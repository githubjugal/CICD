import joblib
import pandas as pd

model = joblib.load("model/model.pkl")

def predict_delay(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return "On Time" if prediction == 1 else "Delayed"
