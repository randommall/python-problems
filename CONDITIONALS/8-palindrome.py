"""
Write a program that checks if a given string is a palindrome 
(reads the same forwards and backwards) using only conditionals.
"""

# Get the input string from the user
input_string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase
cleaned_string = input_string.replace(" ", "").lower()

# Check if the cleaned string is the same when reversed
if cleaned_string == cleaned_string[::-1]:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
