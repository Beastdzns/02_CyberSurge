# src/sentiment_analysis/visualization.py

import matplotlib.pyplot as plt

def plot_sentiment_distribution(predictions):
    """Plot the distribution of sentiment predictions."""
    labels = ['Negative', 'Neutral', 'Positive']
    counts = [list(predictions).count(i) for i in range(len(labels))]

    plt.bar(labels, counts, color=['red', 'gray', 'green'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()
