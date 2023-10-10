"""

Create a program that calculates the sum of all even numbers
 from 1 to 50 using a for loop.
"""

# Initialize a variable to store the sum
sum_of_evens = 0

# Use a for loop to iterate through the numbers from 1 to 50
for num in range(1, 51):
# Check if the number is even (divisible by 2)
    if num % 2 == 0:
        # If it's even, add it to the sum
        sum_of_evens += num

# Print the sum of even numbers
print("Sum of even numbers from 1 to 50:", sum_of_evens)
