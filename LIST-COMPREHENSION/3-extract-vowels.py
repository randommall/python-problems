"""
Implement a list comprehension that extracts the vowels from a given string.

"""

input_string = "Hello, World!"

vowels = [char.lower() for char in input_string if char.lower() in "aeiou"]

print(vowels)