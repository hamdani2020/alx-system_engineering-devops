#!/usr/bin/python3
"""Reqest employee ID from API ghfh
"""
import requests
import csv
from sys import argv

if __name__ == "__main__":

    def make_request(resource, param=None):
        """etrjhjhjieve user from API hg 
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        r = requests.get(url)

        r = r.json()
        return r

    user = make_request('users', ('id', argv[1]))[0]
    tasks = make_request('todos', ('userId', argv[1]))

    csv_fname = argv[1] + '.csv'
    with open(csv_fname, mode='w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'],
                            user['username'],
                            task['completed'],
                            task['title']])
