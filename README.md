# Human Behavior Sentiment Analysis using NLP

## Project Overview

This project analyzes **human behavior and crime-related discussions on social media** using **Natural Language Processing (NLP)** and **Sentiment Analysis**.

The system processes tweet data, cleans the text, identifies crime-related keywords, and evaluates the **public sentiment** expressed in tweets.

The results are visualized through charts and an **interactive Streamlit dashboard**, allowing users to explore crime trends and sentiment patterns.

This project demonstrates a complete **end-to-end data science pipeline** including:

* Data preprocessing
* Crime classification
* Sentiment analysis
* Data visualization
* Interactive dashboard deployment

---

# Project Architecture

```
Tweet Dataset
      ↓
Data Collection
      ↓
Text Preprocessing
      ↓
Crime Classification
      ↓
Sentiment Analysis
      ↓
Data Visualization
      ↓
Interactive Streamlit Dashboard
```

---

# Features

• Tweet text preprocessing using NLP techniques
• Crime type classification from tweet content
• Sentiment analysis using **VADER Sentiment**
• Visualization of crime trends and public reactions
• Interactive **Streamlit dashboard**
• Real-time sentiment prediction for new tweets

---

# Technologies Used

| Category                    | Tools               |
| --------------------------- | ------------------- |
| Programming Language        | Python              |
| Data Processing             | Pandas, NumPy       |
| Natural Language Processing | NLTK                |
| Sentiment Analysis          | VADER Sentiment     |
| Visualization               | Matplotlib, Seaborn |
| Dashboard                   | Streamlit           |
| Machine Learning Utilities  | Scikit-Learn        |

---

# Project Structure

```
human-behavior-sentiment-analysis
│
├── data
│   ├── tweets.csv
│   ├── cleaned_data.csv
│   └── final_data.csv
│
├── src
│   ├── collect_data.py
│   ├── preprocess.py
│   ├── crime_mapper.py
│   ├── sentiment_model.py
│   └── visualization.py
│
├── images
│   ├── dashboard.png
│   ├── heatmap.png
│   └── architecture.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dashboard Features

### Sentiment Distribution

Displays the distribution of tweets into **Positive, Negative, and Neutral sentiment**.

### Crime Type Analysis

Shows frequency of crime categories such as:

* Phishing
* Scam
* Cyber Crime
* Human Trafficking

### City-Based Crime Distribution

Visualizes crime-related tweets across different cities.

### Crime Heatmap

Displays geographic distribution of tweets using **latitude and longitude mapping**.

### Real-Time Sentiment Predictor

Users can input new tweet text and instantly get sentiment prediction.

---

# Dataset

The dataset contains tweet information including:

* tweet text
* username
* location
* follower count
* timestamp

The dataset is preprocessed and transformed into structured data for analysis.

---

# How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/human-behavior-sentiment-analysis.git
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run preprocessing pipeline

```
python src/collect_data.py
python src/preprocess.py
python src/crime_mapper.py
python src/sentiment_model.py
```

### 4. Run the Streamlit dashboard

```
streamlit run app.py
```

---

# Example Dashboard

(Add screenshots here)

```
images/dashboard.png
images/heatmap.png
```

---

# Future Improvements

• Add machine learning based sentiment classification
• Integrate real-time Twitter API data
• Improve geographic crime mapping
• Deploy the application as a live web service

---

# Author

Ansh Kumari
B.Tech CSE (Data Science)

This project was developed to demonstrate skills in **Natural Language Processing, Data Analysis, and Dashboard Development**.