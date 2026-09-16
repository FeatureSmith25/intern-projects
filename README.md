# Student Performance Predictor

Flask web application for student pass/fail prediction, AI-generated study guidance, and study-support chat.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Deploy on Render

1. Create a GitHub repository and upload this project, including `student_performance_model.pkl`.
2. In Render, select New, then Blueprint.
3. Connect the GitHub repository and select `render.yaml`.
4. Add `MISTRAL_API_KEY` to the Render environment settings.
5. Deploy the service.

Render uses `/api/health` to confirm that the web application and prediction model are available.
