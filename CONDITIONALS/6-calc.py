"""
Implement a simple calculator that performs addition, subtraction, multiplication,
 or division based on user input using only conditionals.
"""

# Get the operation choice from the user
print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter the number corresponding to the operation you want to perform: ")

# Get the two numbers from the user as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the selected operation based on user's choice
if choice == '1':
    result = num1 + num2
    operation = "addition"
elif choice == '2':
    result = num1 - num2
    operation = "subtraction"
elif choice == '3':
    result = num1 * num2
    operation = "multiplication"
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "division"
    else:
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Invalid choice. Please choose a valid operation (1, 2, 3, or 4).")
    result = None

# Display the result if it's not None
if result is not None:
    print(f"The result of {num1} {operation} {num2} is: {result}")
