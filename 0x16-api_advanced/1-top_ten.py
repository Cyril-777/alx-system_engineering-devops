#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a given subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'API-Learner'}

    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return print(None)
    children = response.json().get('data').get('children')
    print("\n".join([child.get('data').get('title') for child in children]))
