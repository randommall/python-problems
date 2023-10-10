"""
Implement a list comprehension that flattens a list of lists into a single list.

"""

# List of lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]

# List comprehension to flatten the list
flattened_list = [item for sublist in list_of_lists for item in sublist]

# Print the result
print(flattened_list)
