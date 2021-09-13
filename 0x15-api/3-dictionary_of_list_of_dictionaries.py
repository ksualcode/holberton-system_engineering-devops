#!/usr/bin/python3
''' Script that uses a REST API '''

if __name__ == '__main__':
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/"

    userResponse = requests.get(url + "users").json()

    data = {}
    for user in userResponse:
        id = user["id"]
        username = user["username"]
        data[id] = []
        tasks = requests.get(url+"todos",params={"userId": user["id"]}).json()
        for task in tasks:
            data[id].append({'task': task["title"],
                            'completed': task["completed"],
                            'username': username})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
