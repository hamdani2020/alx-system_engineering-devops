#!/usr/bin/python3
"""This API determines the subreddit sub count
"""

import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """This method requests subreddit recursively using pagination
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = '0x16-api_advanced-hamdani2020'
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': user_agent}

    rq = requests.get(url, headers=headers, allow_redirects=False)

    if rq.status_code != 200:
        return None

    data = rq.json()['data']

    p = data['children']
    for post in p:
        count += 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
