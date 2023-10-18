"""
6
Module-Based Data Processing:
Create a Python module named data_generator.py that contains a function to 
generate a list of 20 random numbers between 1 and 100. In a separate script, 
import the data_generator module and use the generated data to create two lists
 using list comprehensions: one with numbers less than 50 and another with numbers
 greater than or equal to 50. Print all three lists.

"""

import random

def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    return random_numbers