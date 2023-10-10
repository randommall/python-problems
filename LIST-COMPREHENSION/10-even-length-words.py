"""
Create a list comprehension that extracts all the even-length words from a list of strings.

"""

# List of strings
strings = ["apple", "banana", "cherry", "date", "fig", "grape"]

# List comprehension to extract even-length words
even_length_words = [word for word in strings if len(word) % 2 == 0]

# Print the result
print(even_length_words)
