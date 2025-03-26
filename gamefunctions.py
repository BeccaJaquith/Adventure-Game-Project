#CSCI 150 Assignment 9 - Game Loops (Project)
#Rebecca Jaquith
#March 23, 2025


'''This module provides functions to be imported by the game.py file.
'''

import random 


'''Call the print_town_menu() function to print a sign that contains a list of the players current status and avaiable options.'''
def print_town_menu(player_HP, player_gold):
    '''This function prints a list of the players current HP and gold status.
    It also displays three options to progress or end game play.

    Arguments:
    None.

    Return:
    None.

    '''
    
    print(f'/----------------------------------\\')
    print(f'| You are in town.                 |')
    print(f'| Current HP: {player_HP:<15}      |')
    print(f'| Current Gold: {player_gold:<17}  |')
    print(f'| What would you like to do?       |')
    print(f'|                                  |')
    print(f'| 1) Leave town (Fight Monster)    |')
    print(f'| 2) Sleep (Restore HP for 5 Gold) |')
    print(f'| 3) Quit                          |')
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
def monster_fight_menu(monster_HP, player_HP):
    '''This function prints the menu during a monster fight.
    
    Arguements:
    None.

    Return:
    None.

    '''

    print(f'/----------------------------------\\')
    print(f'| Fight the monster!               |')
    print(f'| Monster HP: {monster_HP:<16}     |')
    print(f'| Player HP: {player_HP:<15}       |')
    print(f'|                                  |')
    print(f'| 1) Continue fighting!            |')
    print(f'| 2) Run away!                     |')
    print(f'\\----------------------------------/')


'''Call this function to review monster and player HP before a fight.'''
def monster_fight_HP(monster_HP, player_HP, player_gold):
        '''This function is used to determine the HP.
        If the player equals or is less than zero, they've been defeated.
        If the monster equals or is less than zero, they've been defeated.

        Arguements:
        None.

        Return:
        None.

        '''

        if player_HP <= 0:
            print(f'*****************************************')
            print('You have been defeated!')
            print('You need to sleep in order to fight again.')
            print(f'*****************************************')
            return player_gold
        elif monster_HP <= 0:
            print(f'********************************************')
            print('You defeated the monster! You earned 10 Gold!')
            print(f'********************************************')
            return player_gold + 10
        return player_gold


'''Call this function to select a monster_fight_option.'''
def monster_fight_options(monster_HP, player_HP, player_damage, monster_damage):
        '''This function is used to go over the monster fight options when called.
        
        Arguments:
        None.

        Return:
        None.

        '''

        fight_option = int(input('Please enter menu option 1 or 2:'))

        if fight_option == 1:
            monster_HP -= player_damage
            player_HP -= monster_damage
            print(f'******************************************')
            print(f'You dealt {player_damage} to the monster. ')
            print(f'The monster dealt {monster_damage} to you.')
            print(f'******************************************')
            return (monster_HP, player_HP, 0)
        
        elif fight_option == 2:
            print(f'***************************')
            print('You ran away from the fight!')
            print(f'***************************')
            return (monster_HP, player_HP, 1)

        else:
            print(f'********************************************')
            print('Invalid input. Please enter a valid selection')
            print(f'********************************************')
            return (monster_HP, player_HP, -1)     
        


'''Call fight_monster to fight a monster when player leaves town.'''
def fight_monster(player_HP, player_damage, player_gold):
    '''This function is used to fight a monster.
    The user can choose whether to fight or run away.

    Arguements:
    None.

    Return:
    None.

    '''
    monster_HP = random.randint(5, 50)
    monster_damage = random.randint(5, 10) 

    while (monster_HP > 0 and player_HP > 0):
        monster_fight_menu(monster_HP, player_HP)
        monster_HP, player_HP, flag = monster_fight_options(monster_HP, player_HP, player_damage, monster_damage)
        if flag == 1:
            return (player_HP, player_gold)
        player_gold = monster_fight_HP(monster_HP, player_HP, player_gold)
        check = check_game_over(player_HP, player_gold)
        if check:
            exit()
    return (player_HP, player_gold)


'''Call sleep function to restore player HP.'''
def sleep(player_gold, player_HP):
    '''This function is used to let the player sleep and return to full HP.
    The cost of this is 5 Gold.
    If the player can't afford to sleep, they won't be able to.

    Arguements:
    None.

    Return.
    None.

    '''

    if player_gold >= 5:
        player_HP = 30
        player_gold -= 5
        print(f'**************************************')
        print('You slept and restored your HP to full!')
        print(f'**************************************')
        return (player_HP, player_gold)
    else:
        print(f'************************************')
        print('You do not have enough Gold to sleep.')
        print(f'************************************')
    check = check_game_over(player_HP, player_gold)
    if check:
        exit()


'''Call this function to check if the game is over. HP and Gold == 0.'''
def check_game_over(player_HP, player_gold):
    '''This function checks to see if the player has zero gold and zero HP.
    If so, the game will end.

    Arguments:
    None.

    Return:
    None.

    '''

    if player_HP <= 0 and player_gold <= 0:
        print(f'******************************************')
        print('You have no HP and no Gold left. GAME OVER.')
        print(f'******************************************')
        return True
    return False





