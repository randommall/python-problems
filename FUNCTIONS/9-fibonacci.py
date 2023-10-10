"""
Write a function that generates and returns the first n terms of the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return []
    # Initialize with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1] 

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]

n = 20

fib_sequence = fibonacci(n)

print(fib_sequence)