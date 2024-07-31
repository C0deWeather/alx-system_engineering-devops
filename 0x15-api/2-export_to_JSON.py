#!/usr/bin/python3
"""This script gathers data from a API an exports the data in json format"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    ID = sys.argv[1]
    payload = {'userId': ID}

    t = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=payload
    )
    u = requests.get(f"https://jsonplaceholder.typicode.com/users/{ID}")

    if t.status_code == 200 and u.status_code == 200:
        todo = t.json()
        user = u.json()
        username = user['username']

        for task in todo:
            task['username'] = username
            task['task'] = task.pop('title')

        with open(f"{ID}.json", mode='w') as file:
            fieldnames = ["task", "completed", "username"]
            filtered_todo = [
                {
                    key: task[key]
                    for key in fieldnames
                }
                for task in todo
            ]
            data = {ID: filtered_todo}
            json.dump(data, file)
