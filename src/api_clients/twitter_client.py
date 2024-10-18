# src/api_clients/twitter_client.py

import tweepy

class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweets(self, query, count=100):
        """Fetch recent tweets based on a query."""
        tweets = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q=query, lang='en').items(count):
            tweets.append({
                'text': tweet.text,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name
            })
        return tweets
