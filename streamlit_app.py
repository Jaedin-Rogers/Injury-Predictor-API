import streamlit as st
import requests

st.title("Injury Risk Predictor")

training_hours = st.number_input("Training Hours")
recovery_days = st.number_input("Recovery Days")
fatigue_score = st.number_input("Fatigue Score(1-10)")

if st.button("Predict"):
    res = requests.post(
        "https://injury-predictor-api-production.up.railway.app/predict",
        json={
            "training_hours":training_hours,
            "recovery_days":recovery_days,
            "fatigue_score":fatigue_score
        }
    )
    result = res.json()
    probability = result["probability"]
    risk = result["risk"]
    prob = result.get("probability", 0)

    st.subheader("Result")

    if probability >0.5:
        st.error(f"⚠️ High Injury Risk ({prob:.0%})")
    else:
        st.success(f"✅ Low Injury Risk ({prob:.0%})")

    st.progress(prob)

    if fatigue_score > 7:
        st.warning("High fatigue detected")

    if recovery_days < 2:
        st.warning("Low recovery time detected")

    if training_hours > 30:
        st.warning("High training intensity detected")
