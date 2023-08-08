#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list of all hot articles titles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'API-Learner'}

    params = {"after": after, "count": count}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None
    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    children = data.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after, count)

    return hot_list
