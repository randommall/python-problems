"""
Write a program that prints the reverse of
 a given string using a while loop.
"""

# Input a string from the user
input_string = input("Enter a string: ")

# Initialize variables
length = len(input_string)
reverse_string = ""

# Use a while loop to reverse the string
index = length - 1

while index >= 0:
    reverse_string += input_string[index]
    index -= 1

# Print the reversed string
print("Reversed string:", reverse_string)
