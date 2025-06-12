import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("countries.csv")
plt.figure(figsize=(8,8))
sns.heatmap(df.drop(columns="Country").corr(), annot=True, cmap="coolwarm")

plt.title("Distribution of Average IQ by Country")

plt.tight_layout()

plt.show()