import pandas as pd
import numpy as np

df = pd.read_csv("data/cleaned_data.csv")

def crime_category(text):

    text = str(text).lower()

    if "phishing" in text:
        return "Phishing"

    elif "scam" in text:
        return "Scam"

    elif "cyber" in text:
        return "Cyber Crime"

    elif "trafficking" in text:
        return "Human Trafficking"

    else:
        return "Other"

# Apply crime classification
df["crime_type"] = df["clean_text"].apply(crime_category)

# -------- ADD CITY COLUMN --------
cities = ["Delhi","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad"]
df["city"] = np.random.choice(cities, len(df))

# -------- ADD COORDINATES --------
df["latitude"] = np.random.uniform(8, 37, len(df))
df["longitude"] = np.random.uniform(68, 97, len(df))

# Save dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("Crime classification completed")