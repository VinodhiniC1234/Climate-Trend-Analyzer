import matplotlib.pyplot as plt

def plot_trends(df):
    plt.figure(figsize=(12,6))

    # Temperature trend
    plt.plot(df["date"], df["temperature"], label="Temperature 🌡️", color="red")

    # Rainfall trend
    plt.plot(df["date"], df["rainfall"], label="Rainfall 🌧️", color="blue")

    # Humidity trend
    plt.plot(df["date"], df["humidity"], label="Humidity 💧", color="green")

    plt.title("🌍 Climate Trend Analysis (2010 - 2024)", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Values")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    # Save graph (VERY IMPORTANT for GitHub)
    plt.savefig("outputs/climate_trends.png")

    # Show graph
    plt.show()

    print("✅ Trend graph generated successfully!")