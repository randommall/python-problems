"""
Create a program that checks if a given year is a leap year using only conditionals.
"""

# Get the user's grade as input
grade = input("Enter your grade (A, B, C, D, or F): ")

# Convert the grade to uppercase for case-insensitive comparison
grade = grade.upper()

# Check the grade and print the corresponding message
if grade == 'A':
    print("Excellent")
elif grade == 'B':
    print("Good")
elif grade == 'C':
    print("Average")
elif grade == 'D':
    print("Pass")
elif grade == 'F':
    print("Fail")
else:
    print("Invalid grade. Please enter a valid grade.")
