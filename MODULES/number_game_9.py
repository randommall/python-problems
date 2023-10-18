"""

9
Importing Number Guessing Game:
Create a Python script that imports a module named number_game.py. This 
module generates a random number between 1 and 100 and implements a guessing
 game. Import the module and use it to play the guessing game, tracking the 
number of attempts and providing hints to the user. When the user guesses
 correctly, print the number of attempts and the guessed number.

"""

import random

def play_number_game():
    target_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = input("Guess the number (between 1 and 100): ")
        guess = int(guess)

        attempts += 1

        if guess < target_number:
            print("Try a higher number.")
        elif guess > target_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
