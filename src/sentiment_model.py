import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("data/cleaned_data.csv")

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):

    score = analyzer.polarity_scores(str(text))

    if score["compound"] >= 0.05:
        return "Positive"

    elif score["compound"] <= -0.05:
        return "Negative"

    else:
        return "Neutral"

df["sentiment"] = df["clean_text"].apply(get_sentiment)

df.to_csv("data/final_data.csv", index=False)

print("Sentiment analysis completed")