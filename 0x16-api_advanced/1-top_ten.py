#!/usr/bin/python3
"""This script query Reddit API to determine subreddit sub count
"""

import requests


def top_ten(subreddit):
    """This method requests top ten hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    user_agent = '0x16-api_advanced-hamdani2020'

    headers = {'User-Agent': user_agent}

    rq = requests.get(url, headers=headers, allow_redirects=False)

    if rq.status_code != 200:
        print('None')
    else:
        data = rq.json()['data']
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
