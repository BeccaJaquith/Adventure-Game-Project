'''In this module I will import the gamefunctions.py file and call various functions.
The functions, along with the game.py file will allow the user to play a very basic game.

'''

import gamefunctions
import random
import json
import os



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
    player_gold = 20
    inventory = []
    equipped = []


    
    print(f'/--------------------------------------\\')
    print(f'|{f'Welcome to Becca\'s Adventure Game!':^38}|')
    print(f'|                                      |')
    print(f'| 1) Start New Game                    |')
    print(f'| 2) Load Saved Game                   |')
    print(f'|                                      |')
    print(f'\\--------------------------------------/')

    choice = input("Choose an option: ")

    if choice == "2":
        player_data = gamefunctions.load_game()
        if player_data:
            player_HP = player_data["player_hp"]
            player_gold = player_data["player_gold"]
            inventory = player_data["inventory"]
            equipped = player_data["equipped"]
        else:
            player_HP = 30
            player_gold = 20
            inventory = []
            equipped = []
    else:
        player_HP = 30
        player_gold = 20
        inventory = []
        equipped = []

    while True:

        gamefunctions.print_town_menu(player_HP, player_gold)
        user_choice = gamefunctions.user_selection()
        if user_choice == 1: #Leave town and fight monster.
            player_HP, player_gold, inventory = gamefunctions.fight_monster(player_HP, player_gold, inventory, equipped)
        elif user_choice == 2: #Sleep and restore HP.
            player_HP, player_gold = gamefunctions.sleep(player_gold, player_HP)
        elif user_choice == 3: #Visit the game shop.
            player_gold, inventory = gamefunctions.visit_shop(player_gold, inventory, equipped)
        elif user_choice == 4: #Manage player inventory.
            inventory, equipped = gamefunctions.manage_inventory(inventory, equipped)
        elif user_choice == 5: #Quit the game.
            print(f'/------------------------------------------------\\')
            print(f'|                                                |')
            print(f'|             Thank you for playing!             |')
            print(f'|                                                |')
            print(f'\\------------------------------------------------/')
            gamefunctions.save_game(player_HP, player_gold, inventory, equipped)
            break

if __name__ == "__main__":
    main_game_loop()