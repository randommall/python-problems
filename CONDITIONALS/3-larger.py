"""
Write a Python program that takes two numbers as input and prints the 
larger one using only conditionals.
"""

# Get the two numbers as input
num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

# Check which number is larger
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal.")
