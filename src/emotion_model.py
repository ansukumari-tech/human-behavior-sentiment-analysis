import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/final_data.csv")

def detect_emotion(text):

    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity

    if polarity > 0.4:
        return "joy"
    elif polarity > 0:
        return "trust"
    elif polarity < -0.4:
        return "anger"
    elif polarity < 0:
        return "sadness"
    else:
        return "neutral"

df["emotion"] = df["clean_text"].apply(detect_emotion)

df.to_csv("data/final_data.csv", index=False)

print("Emotion detection completed")
print(df[["clean_text","emotion"]].head())