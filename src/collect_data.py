import pandas as pd

# Load kaggle dataset
df = pd.read_csv("data/tweets.csv")

# Extract tweet text column
if "text" in df.columns:
    tweets = df["text"]
elif "tweet" in df.columns:
    tweets = df["tweet"]
else:
    tweets = df.iloc[:,0]

data = pd.DataFrame()
data["tweet"] = tweets

# Save cleaned structure
data.to_csv("data/cleaned_data.csv", index=False)

print("Tweets prepared successfully")
print(data.head())