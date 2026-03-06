import pandas as pd

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

df["crime_type"] = df["clean_text"].apply(crime_category)

df.to_csv("data/cleaned_data.csv", index=False)

print("Crime classification completed")