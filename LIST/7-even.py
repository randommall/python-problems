"""
Given a list of numbers, count how many of them are even.
"""

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to keep track of the count of even numbers
even_count = 0

# Iterate through the list and count the even numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
# Print the count of even numbers
print("The count of even numbers in the list is:", even_count)