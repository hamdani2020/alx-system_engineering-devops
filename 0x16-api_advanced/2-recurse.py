#!/usr/bin/python3
"""Query Reddit API to determine subred"""
import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """Request subreddit recursively using pagination
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = '0x16-api_advanced-hamdani2020'
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': user_agent}

    rq = requests.get(url, headers=headers, allow_redirects=False)

    if rq.status_code != 200:
        return None

    # load response unit from json
    data = rq.json()['data']

    # extract list of pages
    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
