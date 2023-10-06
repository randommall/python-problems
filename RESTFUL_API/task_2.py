#!/usr/bin/python3

# This library is used for working with JSON data.
import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API for making api requests
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    # retrieves the "username" field from the user's data and stores it in the username variable.
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # opens a JSON file for writing. 
    # "{}.json".format(user_id): This specifies the filename for the JSON file. The {} is a placeholder for the user's ID, which is formatted into the filename. So, if user_id is, for example, "123", it will open a file named "123.json".
    # as jsonfile: This part assigns the opened file to the variable jsonfile. This variable is used as a reference to the open file within the with block.
    with open("{}.json".format(user_id), "w") as jsonfile:

        # This part of the code writes the data_to_export dictionary to the JSON file with indentation for better human readability. Here's what each argument does:
        json.dump(data_to_export, jsonfile, indent=4)

"""Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json"""
