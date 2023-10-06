"""
Create a program that asks the user for their name, age, and favorite color and then prints a message like "Hello, John! You are 25 years old, and your favorite color is blue." using string concatenation.

"""

# Prompt the user for their name
name = input("What is your name? ")

# Prompt the user for their age
age = input("How old are you? ")

# Prompt the user for their favorite color
color = input("What is your favorite color? ")

# Create a personalized message using string concatenation
message = "Hello, " + name + "! You are " + age + " years old, and your favorite color is " + color + "."

# Print the personalized message along with an explanation
# note that you can do it many ways, the focus is to print the right message
print(message)

