# src/sentiment_analysis/preprocessing.py

import re

def clean_text(text):
    """Clean the input text by removing URLs, special characters, and extra whitespace."""
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # Remove mentions and hashtags
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.strip()  # Remove leading/trailing whitespace
    return text

def preprocess_texts(texts):
    """Apply cleaning to a list of texts."""
    return [clean_text(text) for text in texts]
