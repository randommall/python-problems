"""
Implement a program that counts the number of vowels in 
a given string using a for loop.
"""

# Input a string from the user
input_string = input("Enter a string: ")

# Initialize a variable to count the number of vowels
vowel_count = 0

# Define a set of vowels (both uppercase and lowercase)
vowels = set("AEIOUaeiou")

# Use a for loop to iterate through each character in the input string
for char in input_string:
    # Check if the character is in the set of vowels
    if char in vowels:
        vowel_count += 1

# Print the count of vowels
print(f"The number of vowels in the string is: {vowel_count}")
