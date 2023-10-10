"""
Write a program that generates and prints the Fibonacci
 sequence of the first 10 numbers using a for loop.
"""

# Initialize variables to store the first two Fibonacci numbers
fibonacci_sequence = [0, 1]

# Generate the Fibonacci sequence using a for loop
for i in range(2, 10):  # Start from the 3rd number and go up to the 10th number
    next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_number)

# Print the first 10 Fibonacci numbers
print("Fibonacci Sequence (first 10 numbers):")
for num in fibonacci_sequence:
    print(num)