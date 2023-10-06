"""
 Write a program that takes a string and an integer as input and prints a new string, that is the original string repeated that many times as the integer from inpu. For example, if the input is "abc" and 3, the program should print "abcabcabc."
"""

# Prompt the user for input: ask for a string
input_string = input("Enter a string: ")  

# Prompt the user for input: ask for the number of times to repeat the string
# then use the int() function to convert the input to an integer(cos every iput is of type string)
repeat_count = int(input("Enter the number of times to repeat the string: "))  

# Repeat the string by multiplying it by the repetition count
repeated_string = input_string * repeat_count

# Print the repeated string along with an explanation
print(f"Repeated string: {repeated_string}")

