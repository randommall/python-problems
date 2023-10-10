"""
Write a function that finds the greatest common divisor (GCD) of two
 numbers using the Euclidean algorithm.
"""

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

num1 = 18
num2 = 48


gcd_result = gcd_euclidean(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd_result}")