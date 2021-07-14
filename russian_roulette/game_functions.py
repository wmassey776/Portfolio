# -*- coding: utf-8 -*-'
# !/usr/bin/env python
"""
created: 2021-06-12
@author: Will Massey

Project: Russian Roulette/Game functions.
This module contants all the functionality for the Russian Roulette game.
"""

import sys
import time
from gun import Gun
from random import shuffle, choice


def Intro():
    """This function displays the title and game instructions."""
    title = """Welcome to Russian Roulette!
-----------------------------"""

    instructions = """How to Play:    
    • Select 2 to 6 players. 
    • Enter each players' name.
    • Then press enter!
    • The game will automatically play itself    
    • One round consists of each player squeezing the trigger once. 
    • If each player survives, the next round begins.
    • The game ends when a player dies.
-----------------------------"""
    print(title)
    print(instructions)
    
def getPlayers()-> list:
    """ This function first asks for the number of players, then asks for the player's 
    naames. It then returns a list of the player's names."""
    
    # This loop is to ensure valid input.
    while True:  
        numberOfPlayers = input('How many players (2-6)?\n> ')  
        if not numberOfPlayers.isdigit() or not 2 <= int(numberOfPlayers) <= 6:    
            print('Invalid input! Only (2-6) players allowed!', file=sys.stderr)
            continue  # If not valid response, ask again.
        else:
            break       

    # A list to store the player's name.
    playerNames = []
    for i in range(1, int(numberOfPlayers)+1):
        name = input(f"Enter Player {i}'s name: ")           
        playerNames.append(name.title())

    # Welcome players:
    print(f"\nWelcome {', '.join(playerNames[:-1])} and {''.join(playerNames[-1])}!")
    print(f"The gun is loaded... Spin the barrel and begin!\n")
    time.sleep(3)  # a quick pause...
    # Returning a list of players' names.
    return playerNames

def playRound(six_shooter, player_list):
    """ This function evaluates each ROUND, and determines if a player
    lives or dies.

    Pramaters:
        six_shooter (arg: CustomeClass): Represents a six-shooter with one round.
        player_list (list): The list of player names.

    Returns:
        None: Prints player's random survivalMessage, or deathMessage.
    """
    # Tuple of possible Survival messages:       
    survivalMessage = ("got lucky this round!!",
                       "thank heavens you didn't get your brains blown out!",
                       "survives this round!!",
                       "thank goodness you didn't die... YET.",              
                       "lives another day!!")

    # Tuple of possible Death messages:
    deathMessage = ("is DEAD... Too bad!", 
                    "DIED. Good riddance!",                      
                    "needs a bodybag.",               
                    "got splattered. Can somebody clean this mess up?")

    # Tuple of possble Actions
    playerAction = ("picks up the gun and sueezes the trigger.",                    
                    "spins the barrel and sueezes the trigger!",
                    "says a prayer, and nervously pulls the trigger...",
                    "takes a shot of vodka and pulls the trigger!")                  

    round_number = 1  # increments the ROUND number. Starts at ROUND # 1
    # One round consists of each player squeezing the trigger once.

    while six_shooter:        
        print(f"--------[ ROUND #{round_number} ]--------", file=sys.stderr)
        time.sleep(2)
        round_number +=1
        # Loop through all of the player's in player_list
        for player in player_list:
            print(f"It's {player}'s turn: ")
            time.sleep(1)
            print(f"{player} {choice(playerAction)}")
            # This pause is for suspence purposes as the player takes action...
            time.sleep(3)
            # Player spin the barrel, squeezes the trigger and...
            bullet = six_shooter.spin_chamber()
            # If there is a bullet, the player dies and the game ends.
            if bullet:
                # Note: char(128369) is unicode skull & cross bones: 🕱 
                print(f"((((((( {chr(128369)} BANG {chr(128369)} )))))))", file=sys.stderr)  
                print(f"{player} {choice(deathMessage)}")
                print("Game Over!")
                six_shooter = False
                break
            # If no bullet then print a survival message.
            if not bullet:
                print(f"CLICK...")
                time.sleep(1)
                print(f"{player} {choice(survivalMessage)}\n")
            # This is to give a quick pause between rounds.                 
            time.sleep(2)              

def playAgain():
    """Asks if the player wants to play agin."""
    play_again = input('>>> Play again (yes or no)?\n> ')
    if play_again.startswith('n'):
        print('Thanks for playing! до свидания (goodbye)!')
        return False
    else:
        return True
