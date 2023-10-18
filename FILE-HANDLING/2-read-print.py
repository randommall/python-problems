"""
2
Write a program that opens an existing text file, reads its contents, and prints them to the console.

"""

file_name = "output.txt"

file = open(file_name, "r")

if file:
    content = file.read()
    file.close()
    print("File contents:")
    print(content)
else:
    print(f"Error: Unable to open {file_name} for reading.")