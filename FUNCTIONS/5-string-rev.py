"""
Create a function that reverses a given string.
"""
def reverse_string(input_string):
    return input_string[::-1]

original_string = "Hello, World!"

reversed_string = reverse_string(original_string)

print(reversed_string)