"""
write a program that that creates four functions; addition, subtraction,
 multiplication, and division.
create another file and import the functions, use the functions to run
arithmetic problems and print them
"""

# Function to perform addition
def addition(a, b):
    return a + b

# Function to perform subtraction
def subtraction(a, b):
    return a - b

# Function to perform multiplication
def multiplication(a, b):
    return a * b

# Function to perform division
def division(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b