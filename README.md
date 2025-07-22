# 💓 Heart Failure Predictor

A machine learning–powered web application that predicts the risk of heart failure using clinical data. Built during DevTown’s Predictive Modelling Bootcamp, this project combines model training, Flask-based deployment, and a custom web interface.

---

## 📌 Project Overview

- 🔍 **Objective:** Predict whether a patient is at high or low risk of heart failure
- 📊 **Model Accuracy:** Achieved over **80%** on test data
- 🛠️ **Technologies:** Python, Scikit-learn, Flask, HTML/CSS
- 📁 **Dataset:** Heart Failure Clinical Records Dataset

---

## 📂 Project Structure

heart-failure-predictor/
├── app.py # Flask backend
├── model_training.ipynb # Model training notebook
├── model.pkl # Trained model file
├── scaler.pkl # Scaler used for input normalization
├── heart_failure_clinical_records_dataset.csv # Dataset
├── templates/
│ └── index.html # Web form frontend
├── static/
│ └── style.css # Custom CSS styling


---

## 🧠 How It Works

1. User inputs 12 clinical features (age, BP, sodium, etc.)
2. Inputs are scaled and passed to the trained ML model
3. Model predicts the probability of heart failure
4. Result is displayed with an intuitive message & emoji

---

## 💡 Sample Test Inputs

Try this in the form to test a **high-risk** case:

Age: 75
Anaemia: 1
Creatinine Phosphokinase: 500
Diabetes: 1
Ejection Fraction: 25
High Blood Pressure: 1
Platelets: 200000
Serum Creatinine: 2.1
Serum Sodium: 125
Sex: 1
Smoking: 1
Time: 4

yaml
Copy
Edit

👉 Expected Output: 💔 High Risk of Heart Failure





Form Page	Prediction Output

🏁 Built With
🐍 Python

⚙️ Scikit-learn

🌐 Flask

💅 HTML + CSS


🙏 Acknowledgments
DevTown Predictive Modelling Bootcamp
Heart Failure Dataset from Kaggle


