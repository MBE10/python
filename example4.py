import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("countries.csv")

fig = px.scatter_geo(
    df,
    locations = "Country",
    locationmode="country names",
    color="Average_IQ",
    size="GDP",
    hover_name="Country",
    hover_data=["Education_Index","Internet"],
    projection="natural earth",
    title="Distribution of Intelligence & Development Metrics"
)

fig.show()
