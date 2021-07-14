# -*- coding: utf-8 -*-'
# !/usr/bin/env python
"""
created: 2021-06-12
@author: Will Massey
Project: Russian Roulette
"""

import sys

from gun import Gun
from game_functions import Intro, getPlayers, playRound, playAgain

# Introduction and Instructions on how to play the game.
INTRO = Intro()


def main():
    # Set constants:    
    PLAYERS: list = getPlayers()  # A list of Player names.
    SIX_SHOOTER = Gun()  # Represents a gun with a loaded round.
    # Load constants:
    playRound(SIX_SHOOTER, PLAYERS)
    # Play again option:
    if playAgain():
        main()
    else:
        sys.exit()


if __name__ == '__main__':
    main()
