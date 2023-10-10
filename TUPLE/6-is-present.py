"""
Create a program that checks if a specific element is present in a tuple of names.

"""

# Define the tuple of names
names_tuple = ('Alice', 'Bob', 'Charlie', 'David')


# Specify the element you want to check
element_to_check = 'Charlie'


# Check if the element is present in the tuple
if element_to_check in names_tuple:
    print(f'{element_to_check} is present in the tuple.')
else:
    print(f'{element_to_check} is not present in the tuple.')