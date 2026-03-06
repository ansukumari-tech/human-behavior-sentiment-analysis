import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page config
st.set_page_config(page_title="Human Behavior Sentiment Analysis", layout="wide")

# Load dataset
df = pd.read_csv("data/final_data.csv")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Dataset", "Sentiment Predictor"]
)

st.title("Human Behavior Sentiment Analysis")

# ---------------- DASHBOARD ----------------

if option == "Dashboard":

    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tweets", len(df))
    col2.metric("Crime Types", df["crime_type"].nunique())
    col3.metric("Sentiment Types", df["sentiment"].nunique())

    st.subheader("Sentiment Distribution")

    sentiment_counts = df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

    st.subheader("Crime Type vs Sentiment")

    crime_sentiment = df.groupby(["crime_type","sentiment"]).size().unstack()
    st.bar_chart(crime_sentiment)

# ---------------- DATASET ----------------

elif option == "Dataset":

    st.subheader("Dataset Preview")
    st.dataframe(df)

# ---------------- SENTIMENT PREDICTOR ----------------

elif option == "Sentiment Predictor":

    st.subheader("Analyze New Tweet")

    user_input = st.text_area("Enter a tweet")

    if st.button("Predict Sentiment"):

        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(user_input)

        if score["compound"] >= 0.05:
            sentiment = "Positive"
        elif score["compound"] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        st.success(f"Predicted Sentiment: {sentiment}")