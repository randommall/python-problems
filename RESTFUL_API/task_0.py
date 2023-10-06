#!/usr/bin/python3
""" add a clear description here """
import requests
import sys

# This condition ensures that the following code block will only run if the script is executed directly
if __name__ == "__main__":
    # we define the Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID from the command line argument
    employee_id = sys.argv[1]

    # we send an HTTP GET request to the API endpoint that corresponds to the employee's information and stores the response in the user variable.
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # sends an HTTP GET request to the "todos" endpoint with the userId parameter set to the provided employee ID and stores the response in the todos variable.
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    #  initialize an empty list completed to store tasks with completed field True
    completed = []

    # iterate through todos
    for todo in todos:
        # if the completed field of the todo is True
        if todo.get("completed") is True:
            # add it to the initialised completed list
            completed.append(todo.get("title"))

    # here we Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # here we Print the completed tasks one by one with indentation
    for complete in completed:
        print("\t {}".format(completed))

"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)"""
