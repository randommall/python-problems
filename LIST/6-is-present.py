"""
Create a program that checks if a specific element is present in a list of names.
"""

# Define a list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Specify the name you want to check
name_to_check = "Charlie"

# Check if the name is in the list
if name_to_check in names:
    print(f"{name_to_check} is in the list of names.")
else:
    print(f"{name_to_check} is not in the list of names.")