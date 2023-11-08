#!/usr/bin/python3
"""This queries the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user_agent = '0x16-api_advanced-hamdani2020'

    headers = {'User-Agent': user_agent}

    rq = requests.get(url, headers=headers, allow_redirects=False)

    if rq.status_code != 200:
        return 0

    data = rq.json()['data']
    pages = data['children']
    page_data = pages[0]['data']
    return page_data['subreddit_subscribers']
