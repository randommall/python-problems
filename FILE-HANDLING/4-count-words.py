"""
Write a Python script that counts the number of words in a text file.

"""

file_name = "output_2.txt"

file = open(file_name, "r")

if file:
    content = file.read()

    file.close()

    words = content.split()
    word_count = len(words)

    print(f"Number of words in the file: {word_count}")

else:
    print(f"Error: Unable to open {file_name} for reading.")