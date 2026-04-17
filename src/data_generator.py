import pandas as pd
import numpy as np

def generate_climate_data():
    np.random.seed(42)

    dates = pd.date_range(
        start="2010-01-01",
        end="2024-12-31",
        freq="ME"   # IMPORTANT FIX (monthly end)
    )

    n = len(dates)

    temperature = 24 + 0.02*np.arange(n) + np.random.normal(0, 2.5, n)
    rainfall = 100 + 10*np.sin(np.linspace(0, 20, n)) + np.random.normal(0, 15, n)
    humidity = 60 + 5*np.cos(np.linspace(0, 15, n)) + np.random.normal(0, 5, n)

    df = pd.DataFrame({
        "date": dates,
        "temperature": temperature,
        "rainfall": rainfall,
        "humidity": humidity
    })

    df.to_csv("data/climate_data.csv", index=False)

    print("✅ Dataset created successfully!")
    print(df.head())

if __name__ == "__main__":
    generate_climate_data()