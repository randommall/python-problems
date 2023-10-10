"""
Implement a program that calculates the sum of all the digits 
in a given number using a while loop.

"""

# Input a number from the user
num = int(input("Enter a number: "))

# Initialize variables
digit_sum = 0

# Use a while loop to calculate the sum of digits
while num > 0:
    # Extract the last digit using the modulo operator
    last_digit = num % 10
    # Add the last digit to the sum
    digit_sum += last_digit
    # Remove the last digit from the number
    num //= 10

# Print the sum of digits
print("Sum of digits:", digit_sum)
