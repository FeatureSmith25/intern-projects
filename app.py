import os
import json
import re
from pathlib import Path

import joblib
import pandas as pd
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "student_performance_model.pkl"
FEATURES = [
    "Gender",
    "Study_Hours_per_Week",
    "Attendance_Rate",
    "Past_Exam_Scores",
    "Parental_Education_Level",
    "Internet_Access_at_Home",
    "Extracurricular_Activities",
]
ALLOWED_VALUES = {
    "Gender": {"Male", "Female"},
    "Parental_Education_Level": {"High School", "Bachelors", "Masters", "PhD"},
    "Internet_Access_at_Home": {"Yes", "No"},
    "Extracurricular_Activities": {"Yes", "No"},
}

app = Flask(__name__)
model = joblib.load(MODEL_PATH)


def build_student(payload):
    student = {}
    for field in ALLOWED_VALUES:
        value = payload.get(field)
        if value not in ALLOWED_VALUES[field]:
            raise ValueError(f"{field.replace('_', ' ')} has an invalid value.")
        student[field] = value

    numeric_fields = {
        "Study_Hours_per_Week": (0, 168),
        "Attendance_Rate": (0, 100),
        "Past_Exam_Scores": (0, 100),
    }
    for field, limits in numeric_fields.items():
        try:
            value = float(payload.get(field))
        except (TypeError, ValueError):
            raise ValueError(f"{field.replace('_', ' ')} must be a number.")
        if not limits[0] <= value <= limits[1]:
            raise ValueError(f"{field.replace('_', ' ')} must be between {limits[0]} and {limits[1]}.")
        student[field] = value

    return pd.DataFrame([{field: student[field] for field in FEATURES}])


def get_prediction(student):
    prediction = int(model.predict(student)[0])
    probabilities = model.predict_proba(student)[0]
    positions = {int(label): index for index, label in enumerate(model.classes_)}
    pass_probability = float(probabilities[positions[1]])
    fail_probability = float(probabilities[positions[0]])
    risk_level = "High" if fail_probability >= 0.70 else "Medium" if fail_probability >= 0.40 else "Low"
    return {
        "prediction": "Pass" if prediction == 1 else "Fail",
        "pass_probability": round(pass_probability * 100, 1),
        "fail_probability": round(fail_probability * 100, 1),
        "risk_level": risk_level,
    }


def get_ai_support(student, result):
    fallback = {
        "explanation": f"The model estimates a {result['prediction'].lower()} outcome based on the study information provided. This is an estimate for planning, not a certain result.",
        "recommendations": [
            "Attend classes consistently and review missed topics promptly.",
            "Schedule focused study sessions each week and practise weak topics.",
            "Use past exam results to identify one improvement goal at a time.",
        ],
        "study_plan": [
            "Day 1: Review past exam mistakes and set one clear goal.",
            "Day 2: Study the most difficult topic for a focused session.",
            "Day 3: Complete practice questions and check every answer.",
            "Day 4: Review class notes and create short revision notes.",
            "Day 5: Practise another weak topic with timed questions.",
            "Day 6: Review key formulas, concepts, and flashcards.",
            "Day 7: Take a light self-test and plan the next week.",
        ],
        "encouragement": "Small, consistent improvements can make a meaningful difference. Use this estimate as a starting point and keep building your progress.",
    }
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        return fallback

    try:
        from mistralai import Mistral

        prompt = f"""You are a supportive educational assistant. Return only valid JSON with these exact keys: explanation, recommendations, study_plan, encouragement. recommendations must be an array of exactly three concise strings. study_plan must be an array of exactly seven concise strings, each beginning with Day 1 through Day 7. The model estimates {result['prediction']} with {result['pass_probability']}% pass probability and {result['fail_probability']}% fail probability. Risk level: {result['risk_level']}. Student inputs: study hours per week {student.iloc[0]['Study_Hours_per_Week']}, attendance rate {student.iloc[0]['Attendance_Rate']}%, past exam score {student.iloc[0]['Past_Exam_Scores']}. Explain the estimate simply, state it is not certain, avoid inventing personal information, and give practical academic support."""
        client = Mistral(api_key=api_key)
        response = client.chat.complete(
            model=os.getenv("MISTRAL_MODEL", "mistral-small-latest"),
            messages=[
                {"role": "system", "content": "You provide practical, accurate student support."},
                {"role": "user", "content": prompt},
            ],
        )
        support = json.loads(response.choices[0].message.content)
        if not all(key in support for key in fallback):
            return fallback
        if not isinstance(support["recommendations"], list) or not isinstance(support["study_plan"], list):
            return fallback
        return support
    except Exception:
        return fallback


def get_local_chat_response(message):
    """Provide a useful reply if the optional AI provider is unavailable."""
    question = message.strip().lower()

    if any(term in question for term in ("plan", "schedule", "timetable", "routine")):
        return (
            "Yes—you can adjust your study plan whenever it stops fitting your workload. "
            "Keep one fixed daily study block, choose the most urgent topic first, and leave a short catch-up block at the end of the week. "
            "Review the plan each Sunday and change only the parts that did not work."
        )
    if any(term in question for term in ("revision", "revise", "remember", "memor", "forget")):
        return (
            "For better revision, use active recall: close your notes, write what you remember, then check the gaps. "
            "Revisit the same topic after 1 day, 3 days, and 1 week. Short self-quizzes work better than repeatedly rereading notes."
        )
    if any(term in question for term in ("exam", "test", "practice", "question paper")):
        return (
            "Prepare for exams by practising questions under timed conditions. After each set, group mistakes into: concepts you do not know, careless errors, and time-management issues. "
            "Fix one group at a time before attempting another paper."
        )
    if any(term in question for term in ("focus", "concentrat", "distraction", "procrastin")):
        return (
            "Make starting easy: put your phone away, choose one small task, and set a 25-minute timer. "
            "During the break, stand up or get water instead of opening social media. If a task feels too big, reduce it to the first five minutes."
        )
    if any(term in question for term in ("motivat", "stress", "anxious", "tired", "burnout")):
        return (
            "It is normal for motivation to vary. Focus on a small, finishable target today—such as five questions or one page of notes—then take a real break. "
            "Sleep, food, and short movement breaks also make concentration much easier."
        )
    if any(term in question for term in ("time", "busy", "workload", "hours")):
        return (
            "Start by listing your fixed commitments, then reserve three to five focused study blocks each week. "
            "Use the first block for the hardest subject and keep a 15-minute daily review habit so work does not build up."
        )

    topic = re.sub(r"\s+", " ", message.strip())[:120]
    return (
        f"For \"{topic}\", begin with one clear goal and a short focused session. "
        "Then test yourself with a few questions, note what was difficult, and use that to choose your next study task. "
        "Tell me the subject or exam you are preparing for and I can make this more specific."
    )


def get_chat_response(message, history):
    fallback = get_local_chat_response(message)
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        return fallback

    try:
        from mistralai import Mistral

        messages = [{
            "role": "system",
            "content": "You are a supportive student study coach. Answer questions about study plans, revision methods, time management, motivation, and academic recommendations. Be concise, practical, and encouraging. Do not guarantee academic outcomes or invent student details.",
        }]
        for item in history[-8:]:
            if isinstance(item, dict) and item.get("role") in {"user", "assistant"} and isinstance(item.get("content"), str):
                messages.append({"role": item["role"], "content": item["content"][:1000]})
        messages.append({"role": "user", "content": message})
        client = Mistral(api_key=api_key)
        response = client.chat.complete(
            model=os.getenv("MISTRAL_MODEL", "mistral-small-latest"),
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception:
        app.logger.exception("Study-coach AI request failed; using the local response.")
        return fallback


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})


@app.post("/api/predict")
def predict():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Send a JSON request body."}), 400

    try:
        student = build_student(payload)
        result = get_prediction(student)
        result["support"] = get_ai_support(student, result)
        return jsonify(result)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except Exception:
        return jsonify({"error": "The prediction service is temporarily unavailable."}), 500


@app.post("/api/chat")
def chat():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Send a JSON request body."}), 400

    message = payload.get("message", "")
    history = payload.get("history", [])
    if not isinstance(message, str) or not message.strip() or len(message) > 1000:
        return jsonify({"error": "Enter a question between 1 and 1000 characters."}), 400
    if not isinstance(history, list):
        return jsonify({"error": "Conversation history must be a list."}), 400

    return jsonify({"reply": get_chat_response(message.strip(), history)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
