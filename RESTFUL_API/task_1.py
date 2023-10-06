#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format."""
# for reading and writing CSV (Comma-Separated Values) files.
import csv
# make HTTP requests 
import requests
# access to command-line arguments
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API to make the request
    url = "https://jsonplaceholder.typicode.com/"

    # we send an HTTP GET request to the API endpoint that corresponds to the user's information and stores the response in the user variable.
    user = requests.get(url + "users/{}".format(user_id)).json()

    # we retrieve the username from the user data from the api response and store it in username
    username = user.get("username")

    # we send an HTTP GET request to the "todos" endpoint with the userId parameter set to the provided user ID and stores the response in the todos variable.
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # we open a file for writing using the open() function.
    # "{}.csv".format(user_id) is the filename. user_id is formatted into the filename, so if user_id is, for example, "123", it will open a file named "123.csv".
    # "w" indicates that the file should be opened in write mode,
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:

        #  initializes a CSV writer object that will be used to write data to the CSV file
        # csv.writer(csvfile): This part of the code creates a CSV writer object that will write data to the file represented by the csvfile variable.
        # csv.QUOTE_ALL is used, which means that all fields (cells) in the CSV will be enclosed in double quotes. 
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # iterate thorugh a list of todos
        for todo in todos:
            # we use the writer obkect we created earlier to write a single row of data to the csv file.
            # user_id: The ID of the user.
            # username: The username of the user.
            # todo.get("completed"): The completion status of the task True or False.
            # t.get("title"): The title of the task todo.
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])


"""Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv"""
