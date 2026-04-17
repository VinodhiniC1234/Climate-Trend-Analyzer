print("\n🚀 Climate Trend Analyzer Project Starting...\n")

# -----------------------------
# STEP 1: Data Generation
# -----------------------------
from data_generator import generate_climate_data
generate_climate_data()

# -----------------------------
# STEP 2: Load & Clean Data
# -----------------------------
from preprocess import load_and_clean_data
df = load_and_clean_data()

# -----------------------------
# STEP 3: Trend Analysis (Graph)
# -----------------------------
from trend_analysis import plot_trends
plot_trends(df)

# -----------------------------
# STEP 4: Anomaly Detection
# -----------------------------
from anomaly_detection import detect_anomalies
df = detect_anomalies(df)

# -----------------------------
# STEP 5: Forecasting
# -----------------------------
from forecasting import forecast_temperature
df = forecast_temperature(df)

print("\n✅ PROJECT COMPLETED SUCCESSFULLY")
print("📊 Check outputs/ folder for graphs")