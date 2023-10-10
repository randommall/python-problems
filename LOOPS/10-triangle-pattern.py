"""
Create a program that prints a triangle pattern of asterisks using
 nested for loops.
"""

# Define the height of the triangle
height = 10

# Use nested for loops to print the triangle pattern
for i in range(1, height + 1):
    # Print spaces for the left side of the triangle
    for j in range(height - i):
        print(" ", end="")
    # Print asterisks for the right side of the triangle
    for k in range(i):
        print("*", end="")
    # Move to the next line for the next row
    print()
