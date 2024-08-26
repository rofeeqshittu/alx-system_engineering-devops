#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API, based on their employee ID, and exports the data to a CSV file.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py EMPLOYEE_ID")
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

    # Define the CSV filename based on the employee ID
    filename = f"{employee_id}.csv"

    # Writing data to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])

    print(f"Data exported to {filename}")

