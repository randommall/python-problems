"""
 Write a Python program that asks the user
   for a number and prints 
 its multiplication table (up to 10) using a for loop.
"""

# Ask the user for a number
num = int(input("Enter a number: "))

# Use a for loop to print the multiplication table up to 10
print(f"Multiplication table for {num}:")

for i in range(1, 11):
    result = num * i

    print(f"{num} x {i} = {result}")
