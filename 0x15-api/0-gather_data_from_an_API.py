#!/usr/bin/python3
"""script that for a given employee ID, returns information
about his/her TODO list progress"""
import requests
from sys import argv


def todolist(user_id):
    """outputs the employee TODO list progress"""
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)).json().get('name')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)).json()
    completed_tasks = ['\t {}\n'.format(dic.get('title')) for dic in tasks
                       if dic.get('completed')]
    if name and tasks:
        print("Employee {} is done with tasks({}/{}):".format
              (name, len(completed_tasks), len(tasks)))
        print(''.join(completed_tasks), end='')


if __name__ == '__main__':
    if len(argv) == 2:
        todolist(int(argv[1]))
