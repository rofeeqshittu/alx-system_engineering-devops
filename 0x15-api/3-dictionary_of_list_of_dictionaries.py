#!/usr/bin/python3
import json
import requests

def fetch_data(url):
    """Fetch data from the API."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data.")
        return []

def organize_data(tasks):
    """Organize tasks data by user ID."""
    organized_data = {}
    for task in tasks:
        user_id = str(task['userId'])
        if user_id not in organized_data:
            organized_data[user_id] = []
        task_info = {
            "username": task['username'],
            "task": task['title'],
            "completed": task['completed']
        }
        organized_data[user_id].append(task_info)
    return organized_data

def export_to_json(data, filename):
    """Export data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = fetch_data(url)
    if tasks:
        organized_data = organize_data(tasks)
        export_to_json(organized_data, "todo_all_employees.json")

if __name__ == "__main__":
    main()

