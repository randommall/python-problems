"""
Create a list comprehension that filters out all negative numbers from a list.

"""

numbers = [1, -2, 3, -4, 5, -6]

positive_numbers = [x for x in numbers if x >= 0]

print(positive_numbers)