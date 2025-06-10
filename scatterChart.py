import matplotlib.pyplot as plt

countries = ['Singapore', 'Hong Kong', 'South Korea', 'Japan', 'China', 'Switzerland', 'Netherlands', 'Germany']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101]

x_positions = list(range(len(countries)))

plt.figure(figsize=(10,6))
plt.scatter(x_positions, iq_scores, color="orange", s=100)
plt.title("Average IQ by Country (Line Chart)")
plt.xlabel("Country")
plt.ylabel("Average IQ score")
plt.xticks(x_positions,countries, rotation=45)
plt.grid(True)


for i, score in enumerate(iq_scores):
    plt.text(x_positions[i], score + 0.5, str(score), ha='center', va='bottom')

plt.tight_layout()
plt.show()      