"""
Write a function that takes two numbers as arguments and returns their sum.
the parameters must have some default values.

"""

def add_numbers(a=0, b=0):
    return a + b

# call functions without and with arguments:
result1 = add_numbers()   
result2 = add_numbers(3, 4) 
result3 = add_numbers(5)

print(result1 )
print(result2 )
print(result3 )
