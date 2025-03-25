#CSCI 150 Assignment 9 - Game Loops (Project)
#Rebecca Jaquith
#March 23, 2025


'''This module provides functions to be imported by the game.py file.
'''

import random

#Game variables.
player_HP = 30
player_gold = 10
player_damage = random.randint(5, 10) #The damage the player does.
monster_HP = random.randint(5, 50)
monster_damage = random.randint(5, 10) #The damage the monster does.

'''Call the print_town_menu() function to print a sign that contains a list of the players current status and avaiable options.'''
def print_town_menu():
    '''This function prints a list of the players current HP and gold status.
    It also displays three options to progress or end game play.

    Arguments:
    None.

    Return:
    None.

    '''
    #Print the top of the sign border.
    print(f'/----------------------------------\\')

    print(f'| You are in town.                 |')
    print(f'| Current HP: {player_HP:<15}      |')
    print(f'| Current Gold: {player_gold:<17}  |')
    print(f'| What would you like to do?       |')
    print(f'|                                  |')
    print(f'| 1) Leave town (Fight Monster)    |')
    print(f'| 2) Sleep (Restore HP for 5 Gold) |')
    print(f'| 3) Quit                          |')


    #Print the bottom of the border.
    print(f'\\----------------------------------/')

'''Call the user_selection function to recieve a valid input.'''
def user_selection():
    '''This function is used to prompt the user for a valid input.
    
    Arguements:
    None.

    Return:
    user_input = 1, 2, 3
    
    '''
    while True:
         
         try:
             
            user_input = int(input('Please enter menu option 1, 2, or 3:'))
             
            if user_input in range(1, 4):
                return user_input
             
            else:
                print('Invalid input. Please enter a valid selection.')

         except ValueError:
             print('Invalid input. Please enter a valid selection.')


'''Call the function to print the menu during a monster fight.'''
def monster_fight_menu():
    '''This function prints the menu during a monster fight.
    
    Arguements:
    None.

    Return:
    None.

    '''
    global monster_HP, player_HP

    print()
    print('Fight the monster!')
    print(f'Monster HP: {monster_HP}')
    print(f'Player HP: {player_HP}')
    print()
    print('1) Continue fighting!')
    print('2) Run away!')
    print()


'''Call this function to review monster and player HP before a fight.'''
def monster_fight_HP():
        '''This function is used to determine the HP.
        If the player equals or is less than zero, they've been defeated.
        If the monster equals or is less than zero, they've been defeated.

        Arguements:
        None.

        Return:
        None.

        '''

        global monster_HP, player_HP, player_gold

        if player_HP <= 0:

            print()
            print('You have been defeated!')
            print('You need to sleep in order to fight again.')
            print()

        elif monster_HP <= 0:

            print()
            print('You defeated the monster! You earned 10 Gold!')
            print()
            player_gold += 10


'''Call this function to select a monster_fight_option.'''
def monster_fight_options():
        '''This function is used to go over the monster fight options when called.
        
        Arguments:
        None.

        Return:
        None.

        '''

        global monster_HP, player_HP, player_damage, monster_damage
        
        fight_option = int(input('Please enter menu option 1 or 2:'))

        if fight_option == 1:

            monster_HP -= player_damage
            player_HP -= monster_damage

            print()
            print(f'You dealt {player_damage} to the monster.')
            print(f'The monster dealt {monster_damage} to you.')
            print()

        elif fight_option == 2:

            print()
            print('You ran away from the fight!')
            print()

        else:
            print()
            print('Invalid input. Please enter a valid selection')
            print()


'''Call fight_monster to fight a monster when player leaves town.'''
def fight_monster():
    '''This function is used to fight a monster.
    The user can choose whether to fight or run away.

    Arguements:
    None.

    Return:
    None.

    '''
    
    global player_HP, monster_HP, player_gold

    monster_HP = random.randint(5, 50)

    while monster_HP > 0 and player_HP > 0:

        monster_fight_menu()

        monster_fight_options()

        monster_fight_HP()

        check_game_over()

    return


'''Call sleep function to restore player HP.'''
def sleep():
    '''This function is used to let the player sleep and return to full HP.
    The cost of this is 5 Gold.
    If the player can't afford to sleep, they won't be able to.

    Arguements:
    None.

    Return.
    None.

    '''
    global player_gold, player_HP

    if player_gold >= 5:

        player_HP = 30
        player_gold -= 5
        print()
        print('You slept and restored your HP to full!')
        print()
    
    else:

        print()
        print('You do not have enough Gold to sleep.')
        print()

    check_game_over()


'''Call this function to check if the game is over. HP and Gold == 0.'''
def check_game_over():
    '''This function checks to see if the player has zero gold and zero HP.
    If so, the game will end.

    Arguments:
    None.

    Return:
    None.

    '''
    global player_HP, player_gold

    if player_HP <= 0 and player_gold <= 0:

        print()
        print('You have no HP and no Gold left. GAME OVER.')
        print()

        exit()




