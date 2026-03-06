# 📰 Fake News Detection using Machine Learning

## 📌 Project Overview
The **Fake News Detection System** identifies whether a news article is **Real or Fake** using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

The system processes news text, extracts features using **TF-IDF**, and classifies the article using a trained machine learning model.

This project also includes an **interactive Streamlit web application** where users can input news content and instantly receive a prediction.

---

## 🚀 Features

- Detects **Fake vs Real news articles**
- **Text preprocessing pipeline** for cleaning news content
- **TF-IDF feature extraction** for text representation
- Machine Learning based **classification model**
- **Interactive Streamlit dashboard**
- Simple interface for quick news prediction

---

## 🛠 Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **NLTK**
- **TF-IDF Vectorizer**
- **Joblib**
- **Streamlit**

---

## ⚙️ Project Workflow

1. **Data Collection**
2. **Data Preprocessing**
3. **Feature Extraction (TF-IDF)**
4. **Model Training**
5. **Model Evaluation**
6. **Fake News Prediction via Streamlit Dashboard**

---

## 📊 Dataset

**Fake News Dataset (Kaggle)**

Dataset contains:

- **text** → News article content  
- **label** → Real or Fake news

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Data Collection / Preprocessing
```bash
python src/collect_data.py
```

### 3️⃣ Train the Machine Learning Model
```bash
python src/train_model.py
```

### 4️⃣ Run the Streamlit Dashboard
```bash
streamlit run app.py
```

---

## 💡 Future Improvements

- Implement **Deep Learning models (LSTM / BERT)**
- Add **Real-time news scraping**
- **Deploy the model online**
- Improve **dataset size and accuracy**

---

## 📷 Application Interface

Streamlit dashboard allows users to:

- Enter news article text
- Analyze the content
- Instantly get prediction (**Real / Fake News**)

---

## 📄 License

This project is open-source and available for learning and research purposes.