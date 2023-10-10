"""
Given two dictionaries, merge them into a single dictionary.

"""

# Two sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


# Merge dict2 into dict1
dict1.update(dict2)

# dict1 now contains the merged dictionary
print("Merged Dictionary:", dict1)
