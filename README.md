#Fake News Detection using Machine Learning

##Overview
This project detects whether a news article is Real or Fake using Natural Language Processing (NLP) and machine learning.
The system processes news text, extracts features using TF-IDF, and classifies the article using a trained model.

The project also includes a Streamlit web application where users can enter news content and instantly see the prediction.

##Technologies Used
-Python
-Pandas
-Scikit-learn
-NLTK
-TF-IDF Vectorizer
-Joblib
-Streamlit

##Project Workflow
1.Data Collection
2.Data Preprocessing
3.Feature Extraction (TF-IDF)
4.Model Training
5.Model Evaluation
6.Fake News Prediction using Streamlit Dashboard

##Dataset
Fake News Dataset (Kaggle)

Dataset contains:
text → news article content
label → real or fake news

##How to Run
Install dependencies:
pip install -r requirements.txt

Run data collection / preprocessing:
python src/collect_data.py

Train the machine learning model:
python src/train_model.py

Run the Streamlit dashboard:
streamlit run app.py

##Features
Fake vs Real news prediction
Text preprocessing pipeline
TF-IDF feature extraction
Machine learning classification
Interactive Streamlit dashboard

##Future Improvements
Add deep learning models (LSTM / BERT)
Real-time news scraping
Deploy the model online
Improve dataset size and accuracy