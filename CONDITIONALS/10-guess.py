"""
Implement a guessing game where the computer generates a random number between 1 and 100,
 and the user has to guess it using only conditionals.
"""

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")

# Start the game loop
while True:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
