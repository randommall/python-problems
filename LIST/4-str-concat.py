"""
Given a list of strings, concatenate them to form a single string.
"""

# Define a list of strings
strings_list = ["Hello", "world", "!", "This", "is", "a", "list", "of", "strings"]

# Initialize an empty string to store the result
result_string = ""

# Iterate through the list and concatenate the strings
for string in strings_list:
    result_string += string
# Print the concatenated string
print(result_string)
