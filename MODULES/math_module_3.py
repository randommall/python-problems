"""

3
List Operations:
Write a Python script that imports the math module and defines a list of numbers.
 Use a list comprehension to calculate the square root of each number and store 
the results in a new list. Print the original list and the list of square roots.

"""

import math

numbers = [4, 9, 16, 25, 36]

square_roots = [math.sqrt(num) for num in numbers]

print("Original List of Numbers:", numbers)

print("Square Roots:", square_roots)