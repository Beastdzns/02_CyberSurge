# prediction.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Example function for linear regression prediction on stock prices
def linear_regression_prediction(data: pd.DataFrame):
    """
    Perform a linear regression prediction on stock price data.
    
    :param data: DataFrame containing stock prices and other features
    :return: dict containing the model and predictions
    """
    # Assuming 'Close' is the target variable, and all other columns are features
    X = data.drop(columns=['Close'])
    y = data['Close']
    
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict and calculate error
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return {
        'model': model,
        'predictions': y_pred,
        'mse': mse
    }

# Example function for sentiment-based prediction
def sentiment_based_prediction(stock_data: pd.DataFrame, sentiment_data: pd.DataFrame):
    """
    Predict stock price movements based on sentiment analysis and stock data.
    
    :param stock_data: DataFrame containing stock prices
    :param sentiment_data: DataFrame containing sentiment scores
    :return: dict containing the model and predictions
    """
    # Combine stock data and sentiment data
    combined_data = stock_data.copy()
    combined_data['Sentiment_Score'] = sentiment_data['sentiment_score']
    
    X = combined_data.drop(columns=['Close'])
    y = combined_data['Close']
    
    # Train and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Linear regression for simplicity (could use more complex models like LSTM)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return {
        'model': model,
        'predictions': y_pred,
        'mse': mse
    }
