#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API, based on their employee ID, and exports the data to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py EMPLOYEE_ID")
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

    # Extracting employee details
    username = user.get("username")

    # Preparing the data to be written to JSON
    tasks_list = []
    for todo in todos:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    # Creating the final dictionary
    tasks_data = {str(employee_id): tasks_list}

    # Define the JSON filename based on the employee ID
    filename = f"{employee_id}.json"

    # Writing data to the JSON file
    with open(filename, mode='w') as file:
        json.dump(tasks_data, file)

    print(f"Data exported to {filename}")

