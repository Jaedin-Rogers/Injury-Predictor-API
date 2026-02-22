import math

def predict_injury(training_hours, recovery_days, fatigue_score):
    #Predict injury probability using logistic regression formula
    injury_log_odds = (
        (0.1887 * training_hours)
        - (2.0024 * recovery_days)
        + (0.8087 * fatigue_score)
        - 6.9979
    )
    probability = 1 / (1 + math.exp(-injury_log_odds))
    if probability > 0.5:
        risk = 'High'
    elif probability < 0.1:
        risk = 'Low'
    else:
        risk = 'Mid'
    return {
    "probability": float(probability),
    "risk": risk
}
