"""
Write a Python program that checks if a given number is even or odd using only conditionals.
"""

# Get the input number from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
