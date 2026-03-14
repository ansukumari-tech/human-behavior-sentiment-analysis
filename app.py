import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page config
st.set_page_config(page_title="Human Behavior Sentiment Analysis", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/final_data.csv")

df = load_data()

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

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tweets", len(df))
    col2.metric("Positive Tweets", len(df[df["sentiment"]=="Positive"]))
    col3.metric("Negative Tweets", len(df[df["sentiment"]=="Negative"]))
    col4.metric("Neutral Tweets", len(df[df["sentiment"]=="Neutral"]))
    
    # Sentiment distribution
    st.subheader("Sentiment Distribution")

    sentiment_counts = df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

    # Crime vs sentiment
    st.subheader("Crime Type vs Sentiment")

    crime_sentiment = df.groupby(["crime_type","sentiment"]).size().unstack()
    st.bar_chart(crime_sentiment)

    # City analysis
    st.subheader("Crime Distribution by City")

    city_crime = df["city"].value_counts()
    st.bar_chart(city_crime)

    # Map feature
    st.subheader("Crime Sentiment Heatmap")

    if "latitude" in df.columns and "longitude" in df.columns:

        sentiment_filter = st.selectbox(
            "Filter by Sentiment",
            ["All", "Positive", "Negative", "Neutral"]
        )

        if sentiment_filter != "All":
            filtered_df = df[df["sentiment"] == sentiment_filter]
        else:
            filtered_df = df

        st.map(filtered_df[["latitude","longitude"]])

    else:
        st.warning("Location data not available for map visualization.")

# ---------------- DATASET ----------------

elif option == "Dataset":

    st.subheader("Dataset Statistics")
    st.write(df.describe())

# ---------------- SENTIMENT PREDICTOR ----------------

elif option == "Sentiment Predictor":

    st.subheader("Analyze New Tweet")

    tweet_input = st.text_area("Enter Tweet Text")

    analyzer = SentimentIntensityAnalyzer()

    if st.button("Predict Sentiment"):

        score = analyzer.polarity_scores(tweet_input)

        if score["compound"] >= 0.05:
            sentiment = "Positive"
        elif score["compound"] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        st.success(f"Predicted Sentiment: {sentiment}")
        st.write("Sentiment Score:", score)

# ---------------- WORD CLOUD ----------------

from wordcloud import WordCloud
import matplotlib.pyplot as plt

if option == "Dashboard":
    
    st.subheader("Tweet Word Cloud")
    text = " ".join(df["clean_text"].dropna())
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    
    st.pyplot(fig)

# ---------------- DOWNLOAD DATASET BUTTON ----------------

st.download_button(
    "Download Dataset",
    df.to_csv(index=False),
    "crime_sentiment_data.csv"
)

# ---------------- Emotion ----------------

st.subheader("Emotion Distribution")

emotion_counts = df["emotion"].value_counts()
st.bar_chart(emotion_counts)

# ---------------- Emotion Filter ----------------

emotion_filter = st.selectbox(
    "Filter by Emotion",
    ["All"] + list(df["emotion"].unique())
)