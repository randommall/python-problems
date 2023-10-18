"""
Write a program that appends new data to an existing text file.

"""
file_name = "output.txt"

file = open(file_name, "a")

if file:
    data_to_append = "This is the new data to append."

    file.write(data_to_append + "\n")

    file.close()

    print("New data has been successfully appended to the file.")
else:
    print(f"Error: Unable to open {file_name} for appending.")