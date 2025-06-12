import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("average_iq_by_country.csv")
plt.figure(figsize=(8,8))
sns.histplot(data=df, x="Average_IQ", bins=5, kde=True)

plt.title("Distribution of Average IQ by Country")
plt.xlabel("Average IQ")
plt.ylabel("Frequency")
plt.tight_layout()

plt.show()