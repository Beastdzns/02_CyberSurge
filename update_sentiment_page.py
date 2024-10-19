import pandas as pd
import yfinance as yf
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px

# Download VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Define Indian stock tickers and their respective number of shares
tickers_dict = {
    'RELIANCE': 10,
    'TCS': 5,
    'HDFC': 8,
    'INFY': 7,
    'HINDUNILVR': 6,
    'ITC': 4,
    'SBIN': 9,
    'BHARTIARTL': 3,
    'TATAMOTORS': 5,
    'ICICIBANK': 2
}
tickers = tickers_dict.keys()

# Load news headlines 
news_file_path = 'news.csv'  
parsed_and_scored_news = pd.read_csv(news_file_path)

# Perform Sentiment Analysis
vader = SentimentIntensityAnalyzer()
scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()
scores_df = pd.DataFrame(scores)

# Join DataFrames
parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')

# Create a new column for sentiment score
parsed_and_scored_news['sentiment'] = scores_df['compound']

# Fetch current prices and calculate average sentiment per ticker
prices = {}
sentiment_data = {}

for ticker in tickers:
    try:
        # Fetch price for ticker
        tickerdata = yf.Ticker(ticker + '.NS')  # Append '.NS' for Yahoo Finance
        price = tickerdata.history(period="1d")['Close'].iloc[-1]
        prices[ticker] = price

        # Filter news for the specific ticker
        ticker_news = parsed_and_scored_news[parsed_and_scored_news['ticker'].str.contains(ticker, case=False)]
        
        # Calculate average sentiment for the ticker
        avg_sentiment = ticker_news['sentiment'].mean()
        sentiment_data[ticker] = {
            'price': price,
            'average_sentiment': avg_sentiment,
            'headline_count': len(ticker_news)  # Count of headlines for the ticker
        }

        print(f"Fetched price for {ticker}: {price}")  # Debugging statement
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        prices[ticker] = None  # Append None if there's an error

# Prepare DataFrame for treemap
sentiment_df = pd.DataFrame.from_dict(sentiment_data, orient='index').reset_index()
sentiment_df.columns = ['Ticker', 'Price', 'Average Sentiment', 'Headline Count']

# Generate Treemap Plot
fig = px.treemap(
    sentiment_df,
    path=['Ticker'],
    values='Headline Count',
    color='Average Sentiment',
    color_continuous_scale='RdYlGn',
    title='Sentiment Analysis of News Headlines by Ticker'
)

# Save to HTML
output_html_path = 'sentiment_treemap.html'
fig.write_html(output_html_path)

print(f"Treemap plot saved to {output_html_path}.")
