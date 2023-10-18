"""
7
Importing Temperature Converter:
Write a Python script that imports a module named temperature_converter.py.
 This module contains functions to convert between Celsius and Fahrenheit
 temperatures. Use the imported module to convert a user-input temperature 
in one unit to the other. Ensure that error handling for invalid input is
 handled within the temperature_converter module.
"""

def celsius_to_fahrenheit(celsius):
    if type(celsius) in [int, float]:
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    else:
        return "Invalid input. Please enter a valid number for Celsius."

def fahrenheit_to_celsius(fahrenheit):
    if type(fahrenheit) in [int, float]:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    else:
        return "Invalid input. Please enter a valid number for Fahrenheit."
