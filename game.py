#CSCI 150 Assignment 9 - Game Loops (Project)
#Rebecca Jaquith
#March 23, 2025

'''In this module I will import the gamefunctions.py file and call various functions.
The functions, along with the game.py file will allow the user to play a very basic game.
'''

import gamefunctions
import random

'''Call the main_loop_game to view the town menu and play the game.'''
def main_game_loop():
    '''This function allows the user to play the game.
    
    Arguments:
    None.

    Return:
    None.

    '''
    #Game variables.
    player_HP = 30
    player_gold = 10
    player_damage = random.randint(5, 10) #The damage the player does.


    while True:

        gamefunctions.print_town_menu(player_HP, player_gold)
        user_choice = gamefunctions.user_selection()
        if user_choice == 1: #Leave town and fight monster.
            player_HP, player_gold = gamefunctions.fight_monster(player_HP, player_damage, player_gold)
        elif user_choice == 2: #Sleep and restore HP.
            player_HP, player_gold = gamefunctions.sleep(player_gold, player_HP)
        elif user_choice == 3: #Quit the game.
            print()
            print('Thank you for playing the game!')
            print()
            break

if __name__ == "__main__":
    main_game_loop()

