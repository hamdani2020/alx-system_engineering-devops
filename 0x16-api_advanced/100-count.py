#!/usr/bin/python3
"""This request Reddit API to determine the subreddit sub count
"""

import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """The methodd requests subreddit recursively
    """
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                    'count': 0}))

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = '0x16-api_advanced-jmajetich'
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': user_agent}

    rq = requests.get(url, headers=headers, allow_redirects=False)

    if rq.status_code != 200:
        return

    data = rq.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
        keywords_matched = 0
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
