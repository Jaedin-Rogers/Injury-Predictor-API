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
     result = res.json()

        prediction = result["prediction"]
        prob = result.get("probability", 0)

        st.subheader("Result")

        if prediction == 1:
            st.error(f"⚠️ High Injury Risk ({prob:.0%})")
        else:
            st.success(f"✅ Low Injury Risk ({prob:.0%})")

        st.progress(prob)

        if fatigue_score > 7:
            st.warning("High fatigue detected")

        if recovery_days < 2:
            st.warning("Low recovery time detected")
