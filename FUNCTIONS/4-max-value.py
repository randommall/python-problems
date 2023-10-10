"""
Write a function that takes a list of numbers and returns the maximum value in the list.
the parameters must have some default values.

"""

def find_max_value(numbers=[]):
    if not numbers:
        return None  # Return None for an empty list
    else:
        return max(numbers)
    
list1 = []                   # An empty list
list2 = [3, 7, 2, 8, 5]      # A list of numbers

result1 = find_max_value(list1)
result2 = find_max_value(list2)

print(result1)  
print(result2)   