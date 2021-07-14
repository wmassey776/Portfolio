# -*- coding: utf-8 -*-'
# !/usr/bin/env python
"""
created: 2021-06-12
@author: Will Massey
project: Russian Roulette - simple version (no Bullet class)
"""

from random import shuffle
import time
import sys


def main():
    # This represents a six-shooter
    gun = list(range(6))  # Zero will represents the loaded round.

    print('How many players?! ')
    numberOfPlayers = int(input())
    playerNames = []
    for i in range(1, numberOfPlayers + 1):
        name = input(f"Enter player {i}'s name: ")
        playerNames.append(name)

    # Welcome players
    print(f"\nWelcome {''.join(playerNames[:-1])} and {''.join(playerNames[-1])}!")
    print("Let's begin!")
    time.sleep(2)

    # Keeps track of the Round #
    roundNumber = 0

    while gun:
        roundNumber += 1
        print(f'\n--- ROUND {roundNumber} ---')
        for player in playerNames:
            # Spin chamber
            shuffle(gun)
            bullet = gun.pop()

            print(f"It's {player.title()}'s turn!")
            time.sleep(2)

            if bullet == 0:
                print(f'BANG! {player.title()} died!')
                print('Game over!\n')
                gun = False
                break
            if bullet in range(1, 6):
                print('Click...')
                print(f'{player.title()} lives another round.\n')
                time.sleep(2)

    print("Play again (yes or no)?")
    playAgain = input('> ')
    if playAgain == 'no':
        print("Thanks for playing!")
        sys.exit()
    else:
        main()


if __name__ == '__main__':
    main()
