#!/usr/bin/python3
"""a Python script to export data in the JSON format"""

import json
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

    dict = {user_id: []}
    for task in tasks:
        dict[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(user_id), 'w') as j_file:
        json.dump(dict, j_file)
