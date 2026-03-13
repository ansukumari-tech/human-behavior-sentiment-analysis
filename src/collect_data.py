import pandas as pd

df = pd.read_csv("data/tweets.csv")

if "tweets" in df.columns:
    tweets = df["tweets"]
elif "text" in df.columns:
    tweets = df["text"]
elif "tweet" in df.columns:
    tweets = df["tweet"]
else:
    tweets = df.iloc[:,0]

data = pd.DataFrame()
data["tweet"] = tweets

# Clean dataset
data = data.dropna()
data = data.drop_duplicates()

data.to_csv("data/cleaned_data.csv", index=False)

print("Tweets prepared successfully")
print(data.head())