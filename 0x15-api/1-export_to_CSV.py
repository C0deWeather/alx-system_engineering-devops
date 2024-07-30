#!/usr/bin/python3
"""This scripts gathers data from an API an exports the data
in csv format"""

if __name__ == "__main__":
    import csv
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

        with open(f"{ID}.csv", mode='w', newline='') as file:
            fieldnames = ["userId", "username", "completed", "title"]
            filtered_todo = [
                {
                    key: task[key]
                    for key in fieldnames
                }
                for task in todo
            ]
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                quoting=csv.QUOTE_ALL
            )
            writer.writerows(filtered_todo)
