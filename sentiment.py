import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

model = None
vectorizer = None

def train_model():
    global model, vectorizer

    path = os.path.join("data", "reviews.csv")

    df = pd.read_csv(path)

    X = df["review"]
    y = df["sentiment"]

    vectorizer = TfidfVectorizer(stop_words='english')
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

def get_sentiment(text):
    global model, vectorizer

    if model is None:
        train_model()

    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]

    return prediction
