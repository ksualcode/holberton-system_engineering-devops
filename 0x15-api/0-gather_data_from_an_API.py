#!/usr/bin/python3
''' Script that uses a REST API '''

if __name__ == '__main__':
    from sys import argv
    import requests
    import json

    # Getting tasks
    response = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': argv[1]}).json()

    completed = 0
    taskNames = []
    nTasks = 0
    for task in response:
        nTasks += 1
        if task["completed"]:
            completed += 1
            taskNames.append(task["title"])

    # Getting Employee data
    response = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': argv[1]}).json()

    name = response[0]["name"]

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed, nTasks))

    for task in taskNames:
        print("\t" + task)
