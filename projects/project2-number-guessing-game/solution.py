# Project 2 — Number Guessing Game
# Author: your name here

import random

# TODO: generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# TODO: set up a guesses counter
guesses = 0

# TODO: get the user's first guess
guess = int(input("Guess a number between 1 and 10: "))

# TODO: while loop — keep asking until the guess is correct
while guess != secret_number:
    #   - count each guess
    guesses += 1

    #   - print "Too low!" or "Too high!" on each wrong guess
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    #   - get the next guess inside the loop
    guess = int(input("Guess again: "))

# TODO: print the congratulations message with the number of guesses
# We add 1 to guesses to count the final correct guess
print(f"Congratulations! You guessed the number in {guesses + 1} tries.")
