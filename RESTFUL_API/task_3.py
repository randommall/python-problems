#!/usr/bin/python3

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch the list of all users (employees). The response contains a list of users.
    users = requests.get(url + "users").json()

    # Create an empty dictionary to store data for all employees
    data_to_export = {}

    # Iterate through each user in the users list:
    for user in users:
        # Extract the user's ID and save it t0 user_id
        user_id = user["id"]
        # Construct the URL to fetch the user's to-do list based on their ID.
        user_url = url + f"todos?userId={user_id}"
        # Send an HTTP GET request to the user's to-do list endpoint and store the response in the todo_list variable.
        todo_list = requests.get(user_url).json()

        # Create a list of dictionaries where each dictionary represents a task with keys "task" (title of the task), "completed" (completion status), and "username" (the user's username). This list represents the to-do list for the current user.
        #Add the list of tasks to the data_to_export dictionary with the user's ID as the key.
        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    # Return the data_to_export dictionary containing user data and to-do lists.
    return data_to_export


if __name__ == "__main__":
    # we call the fetch_user_data() function and stores the returned data in the data_to_export variable.
    data_to_export = fetch_user_data()

    # opens a JSON file named "todo_all_employees.json" for writing, sets up a JSON writer using json.dump(), and writes the data_to_export dictionary to the JSON file with indentation for better human readability.
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

"""Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json"""
