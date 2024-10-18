# src/api_clients/alpha_vantage.py

import requests

class AlphaVantageClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/query'

    def get_stock_time_series(self, symbol, interval='1min', outputsize='compact'):
        """Fetch time series data for a given stock symbol."""
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': outputsize
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        # Check for errors in the response
        if 'Time Series (1min)' not in data:
            raise ValueError(f"Error fetching data: {data.get('Error Message', 'Unknown error')}")

        return data['Time Series (1min)']
