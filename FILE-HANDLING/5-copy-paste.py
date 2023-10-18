"""
Create a program that copies the contents of one text file into another.

"""

source_file_name = "output.txt"
destination_file_name = "destination.txt"


source_file = open(source_file_name, "r")

destination_file = open(destination_file_name, "w")

if source_file:
    if destination_file:
        content = source_file.read()
        destination_file.write(content)

        source_file.close()
        destination_file.close()
        print(f"File contents copied from {source_file_name} to {destination_file_name}.")
    else:
        print(f"Error: Unable to open {destination_file_name} for writing.")
else:
    print(f"Error: Unable to open {source_file_name} for reading.")