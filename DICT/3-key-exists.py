"""
Write a program to check if a key exists in a dictionary.
"""

# Sample dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Key to check
key_to_check = 'age'

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")