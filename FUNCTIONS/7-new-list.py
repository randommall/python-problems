"""
Create a function that takes a list of numbers and returns a new list with the numbers sorted in ascending order.
"""

def sort_numbers_asc(input_list):
    sorted_list = sorted(input_list)
    return sorted_list


numbers = [5, 2, 9, 1, 8, 3]

sorted_numbers = sort_numbers_asc(numbers)
print(sorted_numbers) 
