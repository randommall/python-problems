"""
3
Create a program that opens a file for writing and adds multiple lines of text to it.

"""

file_name = "output_2.txt"

file = open(file_name, "w")

if file:
    lines_to_write = [
        "This is the first line.",
        "This is the second line.",
        "This is the third line."
    ]
    for line in lines_to_write:
        file.write(line + "\n")

    file.close()

else:
    print(f"Error: Unable to open {file_name} for writing.")