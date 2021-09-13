#!/usr/bin/python3
''' Script that uses a REST API '''

if __name__ == '__main__':
    from sys import argv
    import requests
    import json

    # Getting tasks
    taskResponse = requests.get('https://jsonplaceholder.typicode.com/todos')
    taskResponse = json.loads(taskResponse.text)

    # Getting Employee data
    userResponse = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id': argv[1]})
    userResponse = json.loads(userResponse.text)
    id = userResponse[0]["id"]
    username = userResponse[0]["username"]

    data = {}
    data[id] = []

    for task in taskResponse:
        data[id].append({'task': task["title"], 'completed': task["completed"],
                         'username': username})

    with open(str(id) + '.json', 'w') as file:
        json.dump(data, file)
