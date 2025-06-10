import matplotlib.pyplot as plt

#example data: average IQ score by country

countries = ['Singapore', 'Hong Kong', 'South Korea', 'Japan', 'China', 'Switzerland', 'Netherlands', 'Germany']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101]
colors = ['#a0d8eb', '#96ebc6', '#a1bcf0', '#978ae6', '#956ce0', '#cd7bed', '#f29dfa', '#ed45c9', '#f02b8d', '#ed0e4a']

#create the bar chart

plt.figure(figsize=(10,6))
plt.bar(countries, iq_scores, color=colors)

plt.title("Average IQ by Country")
plt.xlabel("Country")
plt.ylabel("Average IQ score")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
          


