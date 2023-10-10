"""
Remove duplicates from a list of numbers,
 preserving the order of the original list.
"""
# Define a list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Initialize an empty list to store unique values
unique_numbers = []

# Iterate through the original list
for num in numbers:
    # If the number is not already in the unique list, add it
    if num not in unique_numbers:
        unique_numbers.append(num)
print(numbers)
print("unique numbers: ", unique_numbers)