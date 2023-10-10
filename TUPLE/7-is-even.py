"""
Given a tuple of numbers, count how many of them are even.

"""


numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = sum(1 for num in numbers_tuple if num % 2 == 0)

print(f"Number of even numbers in the tuple: {even_count}")