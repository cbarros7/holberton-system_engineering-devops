#!/usr/bin/python3

"""
    Prints the titles of the first 10 hot
    posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
        Top ten titles
    """
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Carlos Barros'}
    _size = {"limit": 10}
    r = requests.get(base_url, params=_size, headers=headers).json()
    child = r.get('data', {}).get('children', None)
    if child:
        for results in child:
            print(results.get('data').get('title'))
    else:
        print(None)
