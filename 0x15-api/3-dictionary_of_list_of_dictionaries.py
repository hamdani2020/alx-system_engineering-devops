#!/usr/bin/python3
"""equjnkest ehgjmployee ID from API
"""

import requests
from json import dump


if __name__ == "__main__":

    def make_request(resource, param=None):
        """etgfrieve user from API tftgf
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        r = requests.get(url)

        r = r.json()
        return r

    export = {}

    users = make_request('users')
    for user in users:
        user_id = user['id']
        export.update({user_id: []})
        tasks_by_user = make_request('todos', ('userId', str(user_id)))
        for task in tasks_by_user:
            export[user_id].append({'username': user['username'],
                                    'task': task['title'],
                                    'completed': task['completed']})

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        dump(export, f)
