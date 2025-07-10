# 🧠 PsychoPredictor AI

**PsychoPredictor AI** is a web-based psychological screening platform that uses advanced machine learning models to predict three key psychological states:

- **Depression Level**
- **Life Satisfaction Level**
- **Big Five Personality Traits**

The system integrates psychometric scales (DASS-21, SWLS, BFI-44) with a hybrid machine learning model (**SVM + XGBoost**) and delivers predictions via a user-friendly frontend using **FastAPI** and **HTML/CSS**.

---

## 🔍 Features

- 🎯 Predicts mental health states from questionnaire responses  
- 📊 Uses a hybrid SVM-XGBoost model for high accuracy  
- 🧪 Supports model interpretability via SHAP  
- 🌐 Frontend built with HTML and integrated via FastAPI backend  
- ⚖️ Includes fairness analysis and demographic breakdown  
- 🧬 Synthetic data generation + SMOTE for balanced training  

---

## 🚀 Live Demo

🖥️ Coming Soon on **Render**  
📎 [Deployment link will be added here when live]

---

## 📂 Project Structure

├── backend/
│ ├── main.py # FastAPI backend with prediction endpoints
│ ├── model/ # Saved ML model (SVM + XGBoost hybrid)
│ └── utils.py # Helper functions (data cleaning, prediction logic)
├── frontend/
│ ├── h.html # Main HTML questionnaire interface
│ └── style.css # Custom styling for the UI
├── data/
│ └── processed_data.csv # Preprocessed and balanced dataset
├── figures/ # Visualizations (SHAP, Confusion Matrices, ROC Curves)
├── README.md
└── requirements.txt # Python dependencies

yaml
## 🛠️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/psycho-predictor-ai.git
cd psycho-predictor-ai

Create a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
bash
pip install -r requirements.txt
▶️ Run the Application

Start the FastAPI Backend
bash
uvicorn backend.main:app --reload

Then open your browser and go to:
cpp
http://127.0.0.1:8000/
View the Frontend
Open frontend/h.html directly or serve it using FastAPI static files.

📈 Machine Learning Pipeline
Synthetic Data Generation using Gaussian Noise Addition (GNA)

Dataset Balancing with SMOTE

Model Training:

Logistic Regression, Decision Tree, SVM, Naive Bayes, XGBoost

Hybrid Model: SVM (Feature Extractor) + XGBoost (Classifier)

Evaluation Metrics:

Accuracy, Precision, Recall, F1 Score, ROC-AUC

Model Interpretation: SHAP values

Fairness Analysis: Gender & Age group comparison

📊 Sample Visuals
📌 Include figures such as:

Confusion Matrix Heatmaps

ROC Curves by Age Group

SHAP Summary Plots

Feature Importance Scores

👨‍🔬 Authors
Yugam Padha

📧 your.email@example.com

🔗 LinkedIn Profile

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
DASS-21, SWLS, and BFI-44 scales

Scikit-learn, XGBoost, SHAP

Render.com for deployment

University research guidance and student feedback

🔒 Disclaimer: This platform is for educational and research purposes only and is not a substitute for clinical diagnosis.

yaml
Let me know if you'd like to:
- Add images or SHAP plots to the README  
- Automatically generate predictions on form submit  
- Include deployment instructions for Render or GitHub Pages

I can tailor this further based on your project updates.
