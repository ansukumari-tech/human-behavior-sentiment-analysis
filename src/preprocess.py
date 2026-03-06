import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

df = pd.read_csv("data/cleaned_data.csv")

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = re.sub(r"http\S+", "", str(text))
    text = re.sub(r"[^a-zA-Z ]", "", text)

    text = text.lower()

    words = text.split()

    words = [w for w in words if w not in stop_words]

    return " ".join(words)

df["clean_text"] = df["tweet"].apply(clean_text)

df.to_csv("data/cleaned_data.csv", index=False)

print("Text preprocessing completed")