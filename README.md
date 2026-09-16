# AI-Driven Student Performance Prediction System

An **AI-assisted academic support system** that predicts a student's academic performance based on their current study and academic information. The system combines **Machine Learning and Generative AI** to provide not only a performance prediction but also personalized recommendations and a practical study plan.

## Live Demo

**Live Application:**
[Student Performance Prediction System](https://intern-projects-theta.vercel.app/?utm_source=chatgpt.com)

---

## Project Overview

Students often know their marks and attendance but may not know how their current academic habits could affect their future performance.

This project aims to solve that problem by analyzing important student-related factors such as:

* Study hours per week
* Attendance rate
* Previous exam score
* Parental education
* Internet access
* Extracurricular activities
* Gender

The system uses these inputs to estimate the student's academic outcome and provide personalized academic guidance.

The application also includes an **AI Study Support Chatbot** that can help students with study planning, revision habits, and practical next steps.

> **Note:** The prediction is an estimate intended for academic planning and should not be considered a guaranteed outcome.

---

## Key Features

### 1. Student Performance Prediction

Students can enter their academic and personal information to generate a performance prediction.

The system considers factors such as:

* Gender
* Parental education
* Study hours per week
* Attendance rate
* Past exam score
* Internet access at home
* Extracurricular activities

### 2. Pass/Fail Probability

The application provides:

* Estimated result
* Pass likelihood
* Fail likelihood
* Prediction confidence

This helps students understand their current performance outlook.

### 3. AI-Based Explanation

Instead of showing only a prediction, the system explains the factors that may influence the student's result.

### 4. Personalized Recommendations

The system generates recommendations based on the student's provided information.

For example, recommendations can focus on:

* Increasing study time
* Improving attendance
* Revision strategies
* Weak academic areas
* Maintaining consistent study habits

### 5. Seven-Day Study Plan

The system generates a practical **7-day study plan** based on the student's current academic situation.

### 6. AI Study Support Chatbot

The integrated study-support chatbot allows students to ask questions related to:

* Study planning
* Revision
* Time management
* Academic improvement
* Next steps for improving performance

---

## System Workflow

```text
Student Information
        ↓
Data Preprocessing
        ↓
Machine Learning Model
        ↓
Performance Prediction
        ↓
Prediction Probability
        ↓
AI Explanation
        ↓
Personalized Recommendations
        ↓
7-Day Study Plan
        ↓
AI Study Support Chatbot
```

---

## Input Features

| Feature                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| Gender                     | Student's gender                            |
| Parental Education         | Education level of parent/guardian          |
| Study Hours                | Average study hours per week                |
| Attendance Rate            | Student's attendance percentage             |
| Past Exam Score            | Previous examination score                  |
| Internet Access            | Availability of internet at home            |
| Extracurricular Activities | Participation in extracurricular activities |

---

## Technology Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Machine Learning Classification Algorithms
* Data Preprocessing
* Feature Engineering
* Model Evaluation

### Generative AI

* Generative AI / LLM
* AI-generated explanations
* Personalized recommendations
* Study-plan generation
* AI study-support chatbot

### Frontend

* Web-based user interface
* Responsive UI
* Form-based student input
* Prediction dashboard
* AI chatbot interface

### Deployment

* Vercel

---

## Machine Learning Pipeline

The Machine Learning component follows a standard ML workflow:

### 1. Data Collection

A student-performance dataset is used to train the prediction model.

### 2. Data Preprocessing

The dataset is cleaned and prepared for machine learning.

Typical preprocessing operations include:

* Handling missing values
* Encoding categorical variables
* Feature selection
* Feature transformation
* Splitting data into training and testing datasets

### 3. Exploratory Data Analysis

The dataset can be analyzed to understand relationships between academic factors and student performance.

Examples:

* Study hours vs performance
* Attendance vs performance
* Previous score vs final result
* Parental education vs performance

### 4. Model Training

Different classification algorithms can be evaluated and the appropriate model can be selected based on evaluation metrics.

### 5. Model Evaluation

The model can be evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### 6. Prediction

After training, the model receives new student information and generates a performance prediction.

---

## Generative AI Layer

The project goes beyond traditional Machine Learning by adding a Generative AI layer.

### Machine Learning

The ML model answers:

> **"What is the predicted academic outcome?"**

### Generative AI

The GenAI component answers:

> **"Why might the student get this outcome, and what can the student do next?"**

This makes the system more useful than a simple prediction model.

The GenAI layer can generate:

* Natural-language explanations
* Personalized recommendations
* Study strategies
* Seven-day study plans
* Conversational academic assistance

---

## Project Architecture

```text
                    ┌──────────────────────┐
                    │      Student         │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │   Web Application    │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │  Student Input Data  │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │ Data Preprocessing   │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │ Machine Learning     │
                    │ Prediction Model     │
                    └──────────┬───────────┘
                               │
                     Prediction + Probability
                               │
                               ↓
                    ┌──────────────────────┐
                    │   Generative AI      │
                    │ Explanation Engine   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ↓                 ↓                 ↓
       Recommendations    Study Plan       AI Chatbot
```

---

## Example Use Case

A student enters:

```text
Study Hours: 18 hours/week
Attendance: 85%
Past Exam Score: 72
Internet Access: Yes
Extracurricular Activities: Yes
Parental Education: Bachelor's
```

The system processes this information and provides:

```text
Estimated Result
       ↓
Pass / Fail Likelihood
       ↓
AI Explanation
       ↓
Personalized Recommendations
       ↓
7-Day Study Plan
```

The student can then continue the conversation with the AI study coach for additional guidance.

---

## Project Objectives

The main objectives of this project are:

1. Predict student academic performance using Machine Learning.
2. Identify factors that may influence academic outcomes.
3. Provide probability-based performance estimates.
4. Generate understandable AI explanations.
5. Provide personalized academic recommendations.
6. Generate a practical seven-day study plan.
7. Provide an interactive AI study-support chatbot.
8. Demonstrate the integration of **Machine Learning + Generative AI** in an educational application.

---

## Future Improvements

The project can be extended with several additional features:

### Early Warning System

Automatically identify students who may require academic support.

### Teacher Dashboard

Teachers could monitor:

* Student performance
* Attendance
* Risk levels
* Improvement trends

### Performance History

Store previous predictions and visualize how a student's performance changes over time.

### More ML Models

Compare multiple algorithms such as:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* Gradient Boosting

### Explainable AI

Integrate techniques such as:

* SHAP
* Feature importance
* Partial dependence analysis

to make model predictions more interpretable.

### Personalized Learning

The system could recommend:

* Learning resources
* Topics to revise
* Practice questions
* Videos
* Study schedules

based on individual weaknesses.

### Voice-Based AI Assistant

Add speech input/output so students can interact with the study coach using voice.

---

## Limitations

* Predictions depend on the quality and representativeness of the training dataset.
* A Machine Learning prediction cannot guarantee a student's actual future result.
* Student performance is influenced by many factors that may not be present in the dataset.
* AI-generated recommendations should be treated as guidance rather than professional academic assessment.

---

## Project Structure

A possible project structure is:

```text
AI-Student-Performance-Prediction/
│
├── data/
│   └── student_performance.csv
│
├── notebooks/
│   └── model_training.ipynb
│
├── model/
│   └── trained_model.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── prediction.py
│   └── ai_support.py
│
├── frontend/
│   ├── components/
│   └── pages/
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact structure should be adjusted according to the actual files and framework used in the repository.

---

## How It Works

1. The student opens the web application.
2. The student enters their academic information.
3. The application sends the information to the prediction system.
4. The Machine Learning model processes the input.
5. The system generates an estimated academic outcome.
6. Prediction probabilities are displayed.
7. Generative AI generates an explanation of the result.
8. Personalized recommendations are provided.
9. A seven-day study plan is generated.
10. The student can interact with the AI study coach for additional support.

---

## Why This Project?

Traditional ML projects often stop after generating a prediction.

This project combines **predictive analytics with Generative AI** to create a more interactive academic-support system.

```text
Traditional ML
     ↓
Prediction

This Project
     ↓
Prediction
     +
Explanation
     +
Recommendations
     +
Study Plan
     +
AI Chatbot
```

This demonstrates how Machine Learning and Generative AI can work together in a practical educational application.

---

## Disclaimer

This application is designed for **educational and academic planning purposes**.

The prediction generated by the system is an estimate based on the information provided by the user and the underlying Machine Learning model. It should not be considered a guaranteed academic result or a substitute for guidance from teachers or academic professionals.

---

## Author

**Hardik Sachan**

B.Tech – Computer Science & Engineering

Interested in:

* Data Science
* Machine Learning
* Generative AI
* Agentic AI
* Artificial Intelligence

---

## License

This project is intended for educational and portfolio purposes.
