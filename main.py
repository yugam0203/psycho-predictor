from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib

# === Initialize FastAPI ===
app = FastAPI()

# === Static & Templates ===
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# === Load Models and Expected Columns ===
dep_model = joblib.load("m/dep_model.pkl")
sat_model = joblib.load("m/sat_model.pkl")
big_model = joblib.load("m/big_model.pkl")
expected_columns = joblib.load("m/expected_columns.pkl")

# === Label Maps (Manual Decoding) ===
depression_map = {
    0: "normal",
    1: "mild",
    2: "moderate",
    3: "severe",
    4: "extremely severe"
}

satisfaction_map = {
    0: "dissatisfied",
    1: "below average",
    2: "average",
    3: "above average",
    4: "high"
}

personality_map = {
    0: "low",
    1: "moderate",
    2: "high"
}

# === Homepage Route ===
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("h.html", {"request": request})

# === Personalized Recommendations for Each Level ===

recommendation_map = {
    "depression": {
        "normal": "You're doing well. Maintain a healthy routine and continue your self-care practices.",
        "mild": "Consider incorporating regular physical activity and mindfulness exercises into your routine.",
        "moderate": "You may benefit from speaking with a counselor or therapist. Journaling and support groups can also help.",
        "severe": "Seek professional help. Therapy and possibly clinical intervention may be beneficial.",
        "extremely severe": "Immediate support is recommended. Please consult a mental health professional as soon as possible."
    },
    "satisfaction": {
        "dissatisfied": "Reflect on areas that cause dissatisfaction. Consider setting small, achievable goals to regain positivity.",
        "below average": "Explore hobbies or connect with others to increase fulfillment in daily life.",
        "average": "You’re in a stable zone. Keep nurturing areas that bring you satisfaction.",
        "above average": "Great job! Continue engaging in meaningful and fulfilling activities.",
        "high": "You’re thriving. Consider mentoring or helping others to share positivity."
    },
    "personality": {
        "low": "Explore personality development resources. Engage in group discussions and reflective practices.",
        "moderate": "You have a balanced personality. Try new experiences to further develop your traits.",
        "high": "Strong personality traits can be influential. Channel them into leadership or creative pursuits."
    }
}

# === Prediction Route ===
@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    try:
        form = await request.form()
        form_data = dict(form)

        question_cols = [f"q{i}" for i in range(1, 41)]
        missing = [q for q in question_cols if q not in form_data]

        # Check if any questions are missing
        if missing:
            return templates.TemplateResponse("h.html", {
                "request": request,
                "error": f"❌ Missing questions: {missing}"
            })

        # Convert inputs to integer
        input_data = {q: int(form_data[q]) for q in question_cols}
        input_df = pd.DataFrame([input_data])

        # Reorder columns to match training
        input_df = input_df[expected_columns]

        # Run predictions
        dep_pred = dep_model.predict(input_df)[0]
        sat_pred = sat_model.predict(input_df)[0]
        big_pred = big_model.predict(input_df)[0]

        # Decode predictions using maps
        depression_label = depression_map.get(dep_pred, "Unknown")
        satisfaction_label = satisfaction_map.get(sat_pred, "Unknown")
        personality_label = personality_map.get(big_pred, "Unknown")

        # Return results page
        return templates.TemplateResponse("results.html", {
            "request": request,
            "depression": depression_label,
            "satisfaction": satisfaction_label,
            "personality": personality_label,
            "recommendation": {
                "dep": recommendation_map["depression"].get(depression_label, "No recommendation available."),
                "sat": recommendation_map["satisfaction"].get(satisfaction_label, "No recommendation available."),
                "big": recommendation_map["personality"].get(personality_label, "No recommendation available.")
             }
        })


    except Exception as e:
        return templates.TemplateResponse("h.html", {
            "request": request,
            "error": f"⚠️ Server Error: {str(e)}"
        })
