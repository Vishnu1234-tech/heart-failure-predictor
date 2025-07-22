from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Extract form input
            features = [
                float(request.form['age']),
                float(request.form['anaemia']),
                float(request.form['creatinine_phosphokinase']),
                float(request.form['diabetes']),
                float(request.form['ejection_fraction']),
                float(request.form['high_blood_pressure']),
                float(request.form['platelets']),
                float(request.form['serum_creatinine']),
                float(request.form['serum_sodium']),
                float(request.form['sex']),
                float(request.form['smoking']),
                float(request.form['time'])
            ]

            # Scale input and predict
            final_features = scaler.transform([features])
            prediction = model.predict(final_features)[0]

            result = "💔 High Risk of Heart Failure" if prediction == 1 else "❤️ Low Risk of Heart Failure"
            return render_template("index.html", prediction_text=result)

        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
