import plotly.express as px

def climate_3d_plot(df):
    fig = px.scatter_3d(
        df,
        x="year",
        y="temperature",
        z="rainfall",
        color="humidity",
        title="🌍 3D Climate Trend Visualization",
        labels={
            "year": "Year",
            "temperature": "Temperature",
            "rainfall": "Rainfall",
            "humidity": "Humidity"
        }
    )

    fig.show()

    print("✅ 3D Visualization Generated Successfully")