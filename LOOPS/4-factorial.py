"""
Create a program that prints the
 factorial of a given number using a while loop.
"""

# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize variables
factorial = 1
current_number = 1

# Calculate the factorial using a while loop
while current_number <= num:
    factorial *= current_number
    current_number += 1

# Print the factorial
print(f"The factorial of {num} is {factorial}")
