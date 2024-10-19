# Stock Market Live Sentiment Dashboard

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Implementation Details](#implementation-details)
    - [Methods Used](#methods-used)
    - [Python Packages Used](#python-packages-used)
- [Steps Followed](#steps-followed)

  
## Project Overview
This project aims to implement a sentiment analysis system that evaluates news headlines related to Indian stock tickers and cryptocurrencies, providing insights into market sentiment. Utilizing VADER from the NLTK library, the system will analyze sentiment scores from news articles, generate an interactive treemap visualization to showcase these sentiments, and fetch current market prices using Yahoo Finance. Additionally, the platform features automated trading capabilities, allowing users to execute buy/sell actions based on predefined sentiment thresholds, enhancing the investment strategy for both stock and cryptocurrency markets. This comprehensive solution empowers retail investors and financial analysts to make informed decisions in real-time.

## Data Source
This project involves scraping a real-time dataset of stock news and information from yahoo finance.

To gather additional information about the stocks, including the Last Closing Price, sector, and industry name, Python is used along with the yfinance library. This library provides the necessary tools and functionalities to retrieve stock data from various sources.


## Implementation Details

### Methods Used
* Data Collection
* Sentiment Analysis
* Data Visualisation

### Python Packages Used
* Pandas
* nltk
* plotly
* yfinance
* BeautifulSoup

## Steps Followed

1. Data Collection: The project collects stock news and retrieves stock information using the yfinance library in Python.
2. Sentiment Analysis: The collected stock news undergoes sentiment analysis using the Vader sentiment analysis tool. This analysis helps determine the sentiment associated with each news article, whether positive, negative, or neutral.
3. Data Visualization: The project utilizes the plotly library to generate data visualizations. These visualizations present the analyzed stock sentiment data in an easily understandable and visually appealing format.
4. Integrating on web app: The project is then integrated on a web app. 
   
