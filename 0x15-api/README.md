## 0x15. API: Python Scripting for Employee Task Data Processing

This project demonstrates the practical application of Python scripting to access and organize employee task data retrieved from an API. Leverage Python's capabilities for data extraction, formatting, and exporting to different formats, gaining experience in data manipulation and automation.


**Project Tasks:**

1. **Gather Data from an API** (**`1_fetch_employee_data.py`**)
    * Craft a Python script using `urllib` or `requests` to retrieve task data for a given employee ID from the specified REST API.
    * Accept an integer as input (employee ID) and display the employee's progress, adhering to the exact formatting requirements.
    * Implement error handling for graceful API interaction.

2. **Export Data to CSV** (**`2_export_to_csv.py`**)
    * Extend the script from Task 1 to export the retrieved data to a CSV file (filename based on the `USER_ID`).
    * The CSV format should be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`

3. **Export Data to JSON** (**`3_export_to_json.py`**)
    * Further enhance the script to export the data in JSON format.
    * The JSON data structure should follow the required format:
    ```json
    {
      "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
      ]
    }
    ```
    * Employ consistent filename format `USER_ID.json`.

4. **Dictionary of List of Dictionaries** (**`4_all_employees_data.py`**)
    * Expand the script's functionality to handle data for all employees.
    * The JSON output should be structured as:
    ```json
    {
      "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
      ],
      "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
      ]
    }
    ```

