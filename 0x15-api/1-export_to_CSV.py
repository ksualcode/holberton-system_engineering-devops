#!/usr/bin/python3
''' Script that uses a REST API '''

if __name__ == '__main__':
    from sys import argv
    import requests
    import json
    import csv

    # Getting tasks
    taskResponse = requests.get('https://jsonplaceholder.typicode.com/todos',
                                params={'userId': argv[1]})
    taskResponse = json.loads(taskResponse.text)

    # Getting Employee data
    userResponse = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id': argv[1]})
    userResponse = json.loads(userResponse.text)
    id = userResponse[0]["id"]
    username = userResponse[0]["username"]

    # Writing the CSV
    with open(str(id) + '.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in taskResponse:
            writer.writerow([id, username, task["completed"], task["title"]])
