"""
Implement a list comprehension that converts a list of temperatures in Celsius to Fahrenheit.

"""

# List of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

fahrenheit_temp = [(c * 9/5) + 32 for c in celsius_temperatures]

print(fahrenheit_temp)