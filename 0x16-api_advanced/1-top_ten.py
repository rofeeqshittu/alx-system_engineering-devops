#!/usr/bin/python3
"""Contains top_ten"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. If not a valid
    subreddit, print None."""
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "myAPI/0.0.1"}

    # Make a GET request to the Reddit API for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # Print the title of each post
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    else:
        print(None)

