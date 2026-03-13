import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords only if missing
try:
    stop_words = set(stopwords.words("english"))
except:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

df = pd.read_csv("data/cleaned_data.csv")

def clean_text(text):

    text = re.sub(r"http\S+", "", str(text))   # remove links
    text = re.sub(r"[^a-zA-Z ]", "", text)     # remove symbols
    text = text.lower()

    words = text.split()

    words = [w for w in words if w not in stop_words]

    return " ".join(words)

# Apply preprocessing
df["clean_text"] = df["tweet"].apply(clean_text)

print("Text preprocessing completed")

# Save dataset
df.to_csv("data/cleaned_data.csv", index=False)