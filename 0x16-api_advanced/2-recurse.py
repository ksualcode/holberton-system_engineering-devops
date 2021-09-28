#!/usr/bin/python3
"""
1-top_ten
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    ''' prints the titles of the first 10 hot posts '''

    url = 'https://www.reddit.com/r/'+subreddit+'/hot.json'
    if (after):
        url = url + '?after=' + after

    response = get(url, headers={'User-Agent': 'UwU'}, allow_redirects=False)
    if (response.status_code == 200):
        for post in response.json()['data']['children']:
            hot_list.append(post['data']['title'])

        next = response.json()['data']['after']

        if (next):
            recurse(subreddit, hot_list, next)
        return hot_list

    return (None)
