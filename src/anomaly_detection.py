from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)

    # Train model on climate features
    df["anomaly"] = model.fit_predict(df[["temperature", "rainfall", "humidity"]])

    # -1 = anomaly, 1 = normal
    anomalies = df[df["anomaly"] == -1]

    print("\n🚨 Anomalies Detected:")
    print(anomalies)

    print(f"\nTotal anomalies found: {len(anomalies)}")

    return df