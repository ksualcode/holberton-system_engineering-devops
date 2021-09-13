#!/usr/bin/python3
''' Script that uses a REST API '''

if __name__ == '__main__':
    from sys import argv
    import requests

    response = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': argv[1]}).json()

    completed = 0
    task_names = []
    n_tasks = 0
    for task in response:
        n_tasks += 1
        if task["completed"]:
            completed += 1
            task_names.append(task["title"])

    response = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': argv[1]}).json()

    name = response[0]["name"]

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed, n_tasks))

    for task in task_names:
        print("\t {}".format(task))
