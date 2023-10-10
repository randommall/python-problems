"""
Implement a function that checks if a number is even and returns True if it is or False if it's odd.
the parameters must have some default values.

"""

def is_even(number=0):
    return number % 2 == 0

result1 = is_even()    
result2 = is_even(3)  
result3 = is_even(8)

print(result1)  
print(result2)  
print(result3)   