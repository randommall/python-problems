"""
Write a program that takes a user's grade as input
 (e.g., 'A', 'B', 'C', 'D', 'F') and prints a corresponding message 
('Excellent', 'Good', 'Average', 'Pass', 'Fail') using only conditionals.
"""

# Get the input year from the user
year = int(input("Enter a year: "))


# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")