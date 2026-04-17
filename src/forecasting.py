import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_temperature(df):
    df = df.copy()

    # Convert time into numeric index
    df["time_index"] = np.arange(len(df))

    # Model
    model = LinearRegression()
    model.fit(df[["time_index"]], df["temperature"])

    # Prediction
    df["forecast_temp"] = model.predict(df[["time_index"]])

    print("\n🔮 Forecasting Completed")
    print(df[["date", "temperature", "forecast_temp"]].head())

    return df