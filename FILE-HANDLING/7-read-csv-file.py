"""
Create a Python script that reads a CSV file and prints the data in tabular form.

"""
import csv

file_name = "data.csv"

csv_file = open(file_name, "r")

if csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print("\t".join(row))

    csv_file.close()
else:
    print(f"Error: Unable to open {file_name} for reading.")