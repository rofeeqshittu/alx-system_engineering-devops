#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, return 0."""
    
    # Set up the headers with a custom User-Agent
    headers = {"User-Agent": "myAPI/0.0.1"}

    # Make a GET request to the Reddit API for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
