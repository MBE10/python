import matplotlib.pyplot as plt

countries = ['Singapore', 'Hong Kong', 'South Korea', 'Japan', 'China', 'Switzerland', 'Netherlands', 'Germany']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101]

plt.figure(figsize=(10,6))
plt.plot(countries, iq_scores, marker='o', linestyle='-', linewidth=2)

plt.title("Average IQ by Country (Line Chart)")
plt.xlabel("Country")
plt.ylabel("Average IQ score")
plt.xticks(rotation=45)
plt.grid(True)

for i, score in enumerate(iq_scores):
    plt.text(countries[i], score + 0.5, str(score), ha='center', va='bottom')

plt.tight_layout()
plt.show()    