"""
Write a Python program that calculates the area of a triangle based on its
 base and height using only conditionals.
"""

# Get the base and height of the triangle as input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Check if the inputs are valid (both positive)
if base > 0 and height > 0:
    # Calculate the area of the triangle
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")
else:
    print("Invalid input. Both base and height must be positive numbers.")
