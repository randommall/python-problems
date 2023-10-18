from data_generator_6 import generate_random_numbers

random_numbers = generate_random_numbers()

less_than_50 = [num for num in random_numbers if num < 50]

greater_than_equal_to_50 = [num for num in random_numbers if num >= 50]

print("Generated Random Numbers:", random_numbers)
print("Numbers Less Than 50:", less_than_50)
print("Numbers Greater Than or Equal to 50:", greater_than_equal_to_50)
