#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API, based on their employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # URLs for fetching user and TODO data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetching data from the API
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Converting the responses to JSON format
    user = user_response.json()
    todos = todos_response.json()

    # Extracting employee name and task details
    employee_name = user.get("name")
    completed_tasks = [todo.get("title") for todo in todos if todo.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Displaying the TODO list progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
