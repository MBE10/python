import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("average_iq_by_country.csv")

countries = df["Country"]
iq_scores = df["Average_IQ"]

plt.figure(figsize=(8,8))
plt.pie(iq_scores, labels=countries, autopct="%1.1f%%", startangle=140)
plt.title("Average Iq Distribuation by Country")
plt.axis("equal")
plt.tight_layout()

plt.show()