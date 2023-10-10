"""
Given two integer variables gotten from user input,
 swap their values without using a third variable."""

num1 = int(input("enter num: "))

num2 = int(input("enter num2: "))

print("before swap num1: ",num1)
print("before swap  num2: ",num2)

# swap values
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("num1: ",num1)
print("num2: ",num2)