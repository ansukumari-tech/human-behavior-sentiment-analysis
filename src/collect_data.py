import pandas as pd

# Load dataset
df = pd.read_csv("data/tweets.csv")

# Detect tweet column
if "tweets" in df.columns:
    tweets = df["tweets"]
elif "text" in df.columns:
    tweets = df["text"]
elif "tweet" in df.columns:
    tweets = df["tweet"]
else:
    tweets = df.iloc[:,0]

# Create standardized dataframe 
data = pd.DataFrame()
data["tweet"] = tweets

# Clean dataset
data = data.dropna()
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("data/cleaned_data.csv", index=False)

#Info
print("Tweets prepared successfully")
print("Total tweets:", len(data))
print("\nSample tweets:")
print(data.head())