# Game: Guess the Number
# Description: This script is a simple and straightforward Python game.
# Players guess a number between 1 and 10. The script provides feedback if the guess is too low or too high,
# and it continues until the correct number is guessed.

# The 'random' module is used for generating random numbers. Documentation: https://docs.python.org/3/library/random.html

import random

number = random.randint(1, 10)  # The computer randomly selects a number between 1 and 10.
guess = 0  # Initialize the guess variable to store user guesses.
print("Welcome to Guess the Number!")
while guess != number:  # Start a loop that continues until the correct number is guessed.
    guess = int(input("Guess a number between 1 and 10: "))  # Prompt the user to enter a guess.
    if guess < number:
         print("Too low. Try again.")  # Inform the user that the guess is too low.
    elif guess > number:
        print("Too high. Try again.")  # Inform the user that the guess is too high.
    else:
        print(f'Congratulations! You guessed the number {number} correctly!')  # Congratulate the user for guessing correctly.


