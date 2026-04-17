import pandas as pd

def load_and_clean_data():
    df = pd.read_csv("data/climate_data.csv")

    df["date"] = pd.to_datetime(df["date"])

    # SAFE METHOD (works in ALL pandas versions)
    df = df.ffill(axis=0)

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    print("✅ Data loaded successfully")
    return df