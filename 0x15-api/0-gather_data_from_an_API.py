#!/usr/bin/python3
"""Using a REST API, for a given employee ID, this script returns
information about their TODO list progress"""

if __name__ == "__main__":
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
        employee_name = user['name']
        total_number_of_tasks = len(todo)
        number_of_done_tasks = sum(
            1 for task in todo if task['completed']
        )
        print(f"Employee {employee_name} is done with tasks\
({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in todo:
            if task['completed']:
                print(f"\t {task['title']}")
