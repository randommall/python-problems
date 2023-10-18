"""
9
Create a program that searches for a specific word in a text file and counts its occurrences.

"""

file_name = "text_file.txt"

search_word = "jungle"

file = open(file_name, "r")

if file:
    content = file.read()
    file.close()
    word_count = content.lower().count(search_word.lower())
    print(f"The word '{search_word}' occurs {word_count} times in the file.")

else:
    print(f"Error: Unable to open {file_name} for reading.")
