import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

try:
    stop_words = set(stopwords.words("english"))
except:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

df = pd.read_csv("data/cleaned_data.csv")

def clean_text(text):

    text = str(text)

    text = re.sub(r"http\S+", "", text)      # remove URLs
    text = re.sub(r"@\w+", "", text)         # remove mentions
    text = re.sub(r"#\w+", "", text)         # remove hashtags
    text = re.sub(r"[^a-zA-Z ]", "", text)   # remove symbols
    text = text.lower()

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)

df["clean_text"] = df["tweet"].apply(clean_text)

print("Text preprocessing completed")
print(df[["tweet","clean_text"]].head())

df.to_csv("data/cleaned_data.csv", index=False)