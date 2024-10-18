# src/api_clients/reddit_client.py

import praw

class RedditClient:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def get_stock_market_posts(self, limit=100):
        """Fetch recent posts from Indian stock market subreddits."""
        subreddits = ['IndianStockMarket', 'IndianStreetBets']
        posts = []
        
        for subreddit in subreddits:
            for submission in self.reddit.subreddit(subreddit).new(limit=limit):
                posts.append({
                    'title': submission.title,
                    'selftext': submission.selftext,
                    'url': submission.url,
                    'created_utc': submission.created_utc,
                    'subreddit': subreddit
                })
        
        return posts
