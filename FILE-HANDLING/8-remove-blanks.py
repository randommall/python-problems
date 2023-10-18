"""
8
Write a program that reads a text file and removes all the blank lines from it.

"""

file_name = "output_2.txt"

file = open(file_name, "r")

if file:
    content = file.readlines()
    file.close()
    non_blank_content = [line.strip() for line in content]

    file = open(file_name, "w")
    if file:
        file.writelines(non_blank_content)
        file.close()
        print("Blank lines removed from the file.")
    else:
        print(f"Error: Unable to open {file_name} for writing.")

else:
    print(f"Error: Unable to open {file_name} for reading.")