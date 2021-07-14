# -*- coding: utf-8 -*-'
# !/usr/bin/env python3
"""
created: 5/29/2021
@author: Will Massey
project: The Number Guessing Game
"""
import sys
from random import randint


def main():
    """This is a guess the number game. """
    # Set up constants
    GUESSES_ALLOWED = 10
    TOTAL_GUESSES = 0
    SECRET_NUMBER = randint(1, 100)

    msg = (f"""\
Hello, and welcome to the Number Guessing Game!
I'm thinking of a secret number between 1 and 100,
and you have a total of {GUESSES_ALLOWED} tries to guess it!\n""")
    print(msg)

    while True:
        guess = input("Enter your guess:\n>>> ")
        if not guess.isdigit():
            print('Please enter a valid number!')
            continue
        # Change guess to an integer:
        guess = int(guess)
        TOTAL_GUESSES += 1
        GUESSES_ALLOWED -= 1

        if guess == SECRET_NUMBER:
            print(f'Congratulations! You guessed the secret number in {TOTAL_GUESSES} tries!')
            break
        if guess > SECRET_NUMBER:
            print("You guessed too high!")
        if guess < SECRET_NUMBER:
            print("You guessed too low!")
        if not GUESSES_ALLOWED:
            print(f"Unfortunately you didn't guess correctly, the secret number was {SECRET_NUMBER}")

    play_again()


def play_again():
    """This function handles the play_again option."""
    while True:
        response = input("PLay again? (y) yes, (n) no:\n>>> ")
        # Keep asking until valid input:
        if response.isdigit() or response not in 'yn':
            print("Invalid response - Select either 'y' or 'n'!")
            continue
        if response == 'y':
            return main()
        else:
            print('Thanks for playing - Goodbye!')
            sys.exit()


if __name__ == '__main__':
    play_again()
