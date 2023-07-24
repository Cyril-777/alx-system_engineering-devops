#!/usr/bin/python3
"""a Python script to export data in the CSV format"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')

    todos_url = url + "/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
