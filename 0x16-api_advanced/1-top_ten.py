#!/usr/bin/python3
"""
1-top_ten
"""

from requests import get


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts '''

    url = 'https://www.reddit.com/r/'+subreddit+'/hot.json'
    response = get(url, headers={'User-Agent': 'UwU'}, allow_redirects=False)
    if (response.status_code == 200):
        for i in range(10):
            postTitle = response.json()['data']['children'][i]['data']['title']
            print(postTitle)
        return

    print("None")
