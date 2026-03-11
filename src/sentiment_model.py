import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("data/cleaned_data.csv")

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):

    score = analyzer.polarity_scores(str(text))

    compound = score["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, compound

# Apply function
df[["sentiment","sentiment_score"]] = df["clean_text"].apply(
    lambda x: pd.Series(get_sentiment(x))
)

# Save final dataset
df.to_csv("data/final_data.csv", index=False)

print("Sentiment analysis completed")