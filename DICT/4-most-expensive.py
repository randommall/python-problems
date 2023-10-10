"""
Given a dictionary of fruits and their prices, find the most expensive fruit.

"""

# Sample dictionary of fruits and their prices
fruits_prices = {
    'apple': 1.0,
    'banana': 0.5,
    'cherry': 2.5,
    'date': 3.0,
    'fig': 2.0
}

# Initialize variables to keep track of the most expensive fruit and its price
most_expensive_fruit = None

# Initialize to negative infinity to ensure any price is higher
max_price = float('-inf')

# Iterate through the dictionary to find the most expensive fruit
for fruit, price in fruits_prices.items():
    if price > max_price:
        max_price = price
        most_expensive_fruit = fruit

# Check if there is at least one fruit in the dictionary
if most_expensive_fruit is not None:
    print(f"The most expensive fruit is '{most_expensive_fruit}' with a price of ${max_price}.")
else:
    print("The dictionary is empty.")