"""
Write a program to find the largest number in a list of integers.
"""
# Define a list of integers
numbers = [10, 4, 7, 23, 15, 42, 8]

# Initialize a variable to store the maximum number, initially set to the first element of the list
max_number = numbers[0]

# Iterate through the list to find the maximum number
for num in numbers:
    if num > max_number:
        max_number = num

# Print the maximum number
print("The largest number in the list is:", max_number)
