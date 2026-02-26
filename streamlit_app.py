import streamlit as st
import requests

st.title("Injury Risk Predictor")

training_hours = st.number_input("training_hours")
recovery_days = st.number_input("recovery_days")
fatigue_score = st.number_input("fatigue_score")

if st.button("Predict"):
    res = requests.post(
        "https://injury-predictor-api-production.up.railway.app/predict",
        json={
            "training_hours":training_hours,
            "recovery_days":recovery_days,
            "fatigue_score":fatigue_score
        }
    )
    st.write(res.json())