# src/sentiment_analysis/finbert_model.py

import torch
from transformers import BertTokenizer, BertForSequenceClassification

class FinBERT:
    def __init__(self, model_name='yiyanghkust/finbert-tone'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)
        self.model.eval()  # Set the model to evaluation mode

    def predict(self, texts):
        inputs = self.tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=1).numpy()  # Get predicted classes
        return predictions  # 0: negative, 1: neutral, 2: positive
