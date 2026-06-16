"""
game.py
--------
A simple number guessing game.
The computer picks a number and the player tries to guess it.
"""

import random

secret = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
