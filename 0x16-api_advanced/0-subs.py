#!/usr/bin/python3

"""
    Write a function that queries the Reddit
    API and returns the number of subscribers.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
        Number of suscribers
    """
    try:
        base_url = 'https://www.reddit.com/r/'
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(
            base_url + '{}/about.json'.format(subreddit), headers=headers)
        return r.json().get('data').get('subscribers')
    except:
        return 0
