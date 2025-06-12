import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("countries.csv")

df_melted = df.melt(id_vars="Country",
                    value_vars=["Average_IQ","GDP","Education_Index","Internet"],
                    var_name="Metric",
                    value_name="Value")

plt.figure(figsize=(10,6))
sns.boxplot(x="Metric", y="Value", data=df_melted)

plt.title("Distribution of Intelligence & Development Metrics")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.tight_layout()

plt.show()