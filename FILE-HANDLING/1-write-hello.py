"""
1
Create a Python script that opens a text file, writes "Hello, World!" to it, and closes the file.

"""

file_name = "output.txt"

file = open(file_name, "w")

if file:
    file.write("Hello, World!")

    file.close()
    print("File has been successfully written.")
else:
    print(f"Error: Unable to open {file_name} for writing.")
