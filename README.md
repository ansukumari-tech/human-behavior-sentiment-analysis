# 🧠 Human Behavior Sentiment Analysis using NLP

## 📌 Project Overview

The **Human Behavior Sentiment Analysis System** analyzes social media tweets to understand public sentiment and behavioral patterns related to crime discussions.

The system processes tweet data, performs **text preprocessing**, detects **crime-related categories**, and applies sentiment analysis to classify tweets as **Positive, Negative, or Neutral**.

The project also includes an **interactive Streamlit web application** where users can explore insights, visualize crime-related sentiment trends, and analyze new tweets in real time.

---

## 🚀 Features

* Analyze public sentiment from tweet text
* Text preprocessing pipeline for cleaning tweet data
* Crime category detection (Phishing, Scam, Cyber Crime, Human Trafficking, etc.)
* Sentiment classification using VADER Sentiment Analyzer
* Interactive Streamlit dashboard for visualization
* Crime distribution analysis by city
* Sentiment distribution and heatmap visualization
* Tweet word cloud for keyword analysis
* Map visualization for crime sentiment locations
* Sentiment prediction tool for new tweets
* Download processed dataset directly from the dashboard

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* VADER Sentiment Analyzer
* Matplotlib
* Seaborn
* Streamlit
* WordCloud
* Scikit-learn
* Joblib

---

## ⚙️ Project Workflow

Data Collection
Data Preprocessing (Text Cleaning & Stopword Removal)
Crime Category Classification
Sentiment Analysis using VADER
Data Visualization & Insights
Interactive Dashboard using Streamlit

---

## 📊 Dataset

Tweet Dataset (CSV Format)

Dataset contains the following important columns:

* **tweet** → Original tweet text
* **clean_text** → Preprocessed tweet text
* **crime_type** → Detected crime category
* **city** → Simulated city location
* **latitude / longitude** → Coordinates used for map visualization
* **sentiment** → Predicted sentiment label
* **sentiment_score** → VADER compound sentiment score

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run Data Preparation

```
python collect_data.py
```

### 3️⃣ Run Text Preprocessing

```
python preprocess.py
```

### 4️⃣ Run Crime Classification

```
python crime_mapper.py
```

### 5️⃣ Run Sentiment Analysis

```
python sentiment_model.py
```

### 6️⃣ Launch the Streamlit Dashboard

```
streamlit run app.py
```

The application will open in your browser.

---

## 📷 Application Interface

The Streamlit dashboard allows users to:

* View dataset statistics and metrics
* Analyze sentiment distribution
* Explore crime vs sentiment relationships
* Visualize crime distribution by city
* View tweet keyword word cloud
* Explore tweet locations on a map
* Enter a new tweet and predict its sentiment

---

## 💡 Future Improvements

* Implement Deep Learning models (LSTM / BERT)
* Integrate real-time tweet collection using Twitter API
* Improve crime classification using machine learning models
* Add advanced geospatial crime heatmap visualizations
* Deploy the application to cloud platforms

---

## 👩‍💻 Author

**Ansu Kumari**
B.Tech – Computer Science & Engineering
Brainware University

---

## 📄 License

This project is open-source and intended for **educational and research purposes**.