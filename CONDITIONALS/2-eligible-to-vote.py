"""
Create a program that asks the user for their age and then determines
 if they are eligible to vote (18 years or older) using only conditionals.
"""

# Get the user's age as input
age = int(input("Please enter your age: "))

# Check if the age is 18 or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
