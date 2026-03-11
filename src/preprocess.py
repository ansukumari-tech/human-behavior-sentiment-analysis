import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import numpy as np

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

# Clean tweet text
df["clean_text"] = df["tweet"].apply(clean_text)

print("Text preprocessing completed")

# ---------------------------------------------------
# NEW FEATURE: Generate coordinates for heatmap
# ---------------------------------------------------

# Simulate locations across India
df["latitude"] = np.random.uniform(8, 37, len(df))
df["longitude"] = np.random.uniform(68, 97, len(df))

print("Coordinates generated for heatmap")

# Save dataset
df.to_csv("data/cleaned_data.csv", index=False)