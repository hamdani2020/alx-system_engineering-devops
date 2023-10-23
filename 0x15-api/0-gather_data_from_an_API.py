#!/usr/bin/python3
"""This script request for employee ID from API
"""

from sys import argv
import requests
from json import load


if __name__ == "__main__":

    def make_request(resource, param=None):
        """It retrieves user from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        rq = requests.get(url)
        rq = rq.json()
        return rq

    user = make_request('users', ('id', argv[1]))
    tasks = make_request('todos', ('userId', argv[1]))
    tasks_completed = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))
