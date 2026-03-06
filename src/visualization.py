import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/final_data.csv")

# Sentiment Distribution
plt.figure(figsize=(6,6))
df["sentiment"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Overall Sentiment Distribution")
plt.ylabel("")
plt.show()

# Crime vs Sentiment Heatmap
plt.figure(figsize=(8,5))
crime_sentiment = pd.crosstab(df["crime_type"], df["sentiment"])

sns.heatmap(crime_sentiment, annot=True, cmap="coolwarm")

plt.title("Crime Type vs Sentiment Heatmap")
plt.show()