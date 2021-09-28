#!/usr/bin/python3
"""
0-subs
"""

from requests import get


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers of a subreddit '''

    url = 'https://www.reddit.com/r/'+subreddit+'/about.json'
    response = get(url, headers={'User-Agent': 'UwU'}, allow_redirects=False)
    if (response.status_code == 200):
        return (response.json()['data']['subscribers'])

    return 0
