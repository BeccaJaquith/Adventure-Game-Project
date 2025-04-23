'''This module provides functions to be imported by the game.py file.

'''

import random 
import json
import map_module
import wanderingMonster

#-------------------------Town Menu-------------------------#
'''Call the print_town_menu() function to print a sign that contains a list of the players current status and avaiable options.'''
def print_town_menu(player_HP, player_gold):
    '''This function prints a list of the players current HP and gold status.
    It also displays three options to progress or end game play.

    Arguments:
    player_HP, player_gold

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
    print(f'| 3) Visit Shop                    |')
    print(f'| 4) Manage Inventory              |')
    print(f'| 5) Save and Quit                 |')
    print(f'\\----------------------------------/')

'''Call the user_selection function to recieve a valid input.'''
def user_selection():
    '''This function is used to prompt the user for a valid input.
    
    Arguments:
    None.

    Return:
    user_input = 1, 2, 3, 4, 5
    
    '''
    while True:
         try:
            user_input = int(input('Please enter menu option 1, 2, 3, 4 or 5:'))
            if user_input in range(1, 6):
                return user_input
            else:
                print_invalid_input()

         except ValueError:
                print_invalid_input()


#-------------------------Combat-------------------------#
'''Call the function to print the menu during a monster fight.'''
def monster_fight_menu(monster_HP, player_HP, monster_name):
    '''This function prints the menu during a monster fight.
    
    Arguments:
    monster_HP, player_HP

    Return:
    None.

    '''

    print(f'/----------------------------------\\')
    print(f'| {f"Fight the {monster_name}!":<33}|')
    print(f'| Monster HP: {monster_HP:<16}     |')
    print(f'| Player HP: {player_HP:<15}       |')
    print(f'|                                  |')
    print(f'| 1) Continue fighting!            |')
    print(f'| 2) Use a Health Potion!          |')
    print(f'| 3) Use a Poison Arrow!           |')
    print(f'| 4) Use a Magic Scroll!           |')
    print(f'| 5) Run away!                     |')
    print(f'\\----------------------------------/')


'''Call this function to review monster and player HP before a fight.'''
def monster_fight_HP(monster_HP, player_HP, player_gold):
        '''This function is used to determine the HP.
        If the player equals or is less than zero, they've been defeated.
        If the monster equals or is less than zero, they've been defeated.

        Arguments:
        monster_HP, player_HP, player_gold

        Return:
        player_gold

        '''

        if player_HP <= 0:
            print(f'/-------------------------------------------------\\')
            print(f'|                                                 |')
            print(f'|             YOU HAVE BEEN DEFEATED!             |')
            print(f'|    You need to sleep in order to fight again.   |')
            print(f'|                                                 |')
            print(f'\\-------------------------------------------------/')
            return player_gold
        elif monster_HP <= 0:
            print(f'/-------------------------------------------------\\')
            print(f'|                                                 |')
            print(f'|            You defeated the monster             |')
            print(f'|              and took their Gold!               |')
            print(f'|                                                 |')
            print(f'\\-------------------------------------------------/')
            player_gold = player_gold + random.randint(10, 50)
            return player_gold
        return player_gold


'''Call this function to select a monster_fight_option.'''
def monster_fight_options(monster_HP, player_HP, inventory, equipped, monster):
        '''This function is used to go over the monster fight options when called.
        
        Arguments:
        monster_HP, player_HP, inventory

        Return:
        monster_HP, player_HP, inventory

        '''

        has_potion = any(item.get('name') == 'Health Potion' for item in inventory)
        has_poison = any(item.get('name') == 'Poison Arrow' for item in inventory)
        has_magic = any(item.get('effect') == 'instant kill' for item in inventory)

        fight_option = input("Please enter menu option 1, 2, 3, 4 or 5:")

        if fight_option == '1':
            total_damage_reduction = 0 #Damage reduction to player.
            total_damage_increase = 0 #Damage increase to monster.
            for item in equipped:
                if item['item type'] == 'Weapon':
                    total_damage_increase += item['damage']
                    item['current_durability'] -= 1
                    if item['current_durability'] < 1:
                        print(f'/-------------------------------------------------\\')
                        print(f'|                                                 |')
                        print(f'|             Your weapon just broke!             |')
                        print(f'|           Buy another one at the shop!          |')
                        print(f'|                                                 |')
                        print(f'\\-------------------------------------------------/')
                        equipped.pop(equipped.index(item))
                if item['item type'] == 'Armor':
                    total_damage_reduction += item['reduction']
                    item['current_durability'] -= 1
                    if item['current_durability'] < 1:
                        print(f'/-------------------------------------------------\\')
                        print(f'|                                                 |')
                        print(f'|             Your shield just broke!             |')
                        print(f'|           Buy another one at the shop!          |')
                        print(f'|                                                 |')
                        print(f'\\-------------------------------------------------/')
                        equipped.pop(equipped.index(item))

            monster_damage = monster.damage - total_damage_reduction #Damage done by monster.
            if monster_damage < 0:
                monster_damage = 0
            player_damage = random.randint(0, 10) + total_damage_increase #Damage done by player.
            monster_HP -= player_damage
            player_HP -= monster_damage
            print()
            print(f'/-------------------------------------------------\\')
            print(f'|                                                 |')
            print(f'|{f"You dealt {player_damage} damage to the monster.":^49}|')
            print(f'|{f"The monster dealt {monster_damage} damage to you.":^49}|')
            print(f'|                                                 |')
            print(f'\\-------------------------------------------------/')
            return (monster_HP, player_HP, inventory, equipped, 0)
        
        elif fight_option == '2' and has_potion:
            for item in inventory:
                if item['name'] == 'Health Potion':
                    potion_power = item['effect']['player_HP']
                    player_HP += potion_power
                    inventory[inventory.index(item)]['amount'] -= 1
                    if item['amount'] < 1:
                        inventory.remove(item)
                    print(f'/----------------------------------------------------\\')
                    print(f'|                                                    |')
                    print(f'|{f"You used a Health Potion! Player HP increased by {potion_power}!":^52}|')
                    print(f'|                                                    |')
                    print(f'\\----------------------------------------------------/')
                    return monster_HP, player_HP, inventory, equipped, 0
        elif fight_option == '2' and not has_potion:    
            print(f'/------------------------------------------------\\')
            print(f'|                                                |')
            print(f'|       This item is not in your inventory.      |')
            print(f'|                                                |')
            print(f'|           Select a different option.           |')
            print(f'|                                                |')
            print(f'\\------------------------------------------------/')
            return monster_HP, player_HP, inventory, equipped, 0

        elif fight_option == '3' and has_poison:
            for item in inventory:
                if item['name'] == 'Poison Arrow':
                    poison_effect = item['effect']['monster_HP']
                    monster_HP -= poison_effect
                    inventory[inventory.index(item)]['amount'] -= 1
                    if item['amount'] < 1:
                        inventory.remove(item)
                    print(f"\nYou used a Poison Arrow! Monster HP reduced by {poison_effect}.")
                    print(f'/----------------------------------------------------\\')
                    print(f'|                                                    |')
                    print(f'|{f"You used a Poison Arrow! Monster HP reduced by {poison_effect}!":^52}|')
                    print(f'|                                                    |')
                    print(f'\\----------------------------------------------------/')
                    return monster_HP, player_HP, inventory, equipped, 0
            
        elif fight_option == '3' and not has_poison:
                print(f'/------------------------------------------------\\')
                print(f'|                                                |')
                print(f'|       This item is not in your inventory.      |')
                print(f'|                                                |')
                print(f'|           Select a different option.           |')
                print(f'|                                                |')
                print(f'\\------------------------------------------------/')
                return monster_HP, player_HP, inventory, equipped, 0

        elif fight_option == '4' and has_magic:
            for item in inventory:
                if item.get('effect') == 'instant kill':
                    print(f'/-------------------------------------------------\\')
                    print(f'|                                                 |')
                    print(f'|{f"You used a {item['name']} to defeat the monster!":^49}|')
                    print(f'|                                                 |')
                    print(f'\\-------------------------------------------------/')
                    inventory[inventory.index(item)]['amount'] -= 1
                    if item['amount'] < 1:
                        inventory.remove(item)
                    return 0, player_HP, inventory, equipped, 0
    
        elif fight_option == '4' and not has_magic:
            print(f'/------------------------------------------------\\')
            print(f'|                                                |')
            print(f'|       This item is not in your inventory.      |')
            print(f'|                                                |')
            print(f'|           Select a different option.           |')
            print(f'|                                                |')
            print(f'\\------------------------------------------------/')
            return monster_HP, player_HP, inventory, equipped, 0

        elif fight_option == '5':
            print(f'/------------------------------------------------\\')
            print(f'|                                                |')
            print(f'|          You ran away from the fight!          |')
            print(f'|                                                |')
            print(f'\\------------------------------------------------/')
            return (monster_HP, player_HP, inventory, equipped, 1)

        else:
            print_invalid_input()
            return (monster_HP, player_HP, inventory, equipped, -1)     
        

'''Call fight_monster to fight a monster when player leaves town.'''
def fight_monster(player_HP, player_gold, inventory,equipped, monster):
    '''This function is used to fight a monster.
    The user can choose whether to fight or run away.

    Arguments:
    player_HP, player_gold, inventory, equipped

    Return:
    player_HP, player_gold, inventory

    '''
    monster_HP = monster.hp

    print(f'/------------------------------------------------\\')
    print(f'|                                                |')
    print(f'|{f"A {monster.name} with {monster_HP} HP appears!":^48}|')
    print(f'|                                                |')
    print(f'\\------------------------------------------------/')

    while (monster_HP > 0 and player_HP > 0):
        monster_fight_menu(monster_HP, player_HP, monster.name)
        monster_HP, player_HP, inventory, equipped, flag = monster_fight_options(monster_HP, player_HP, inventory, equipped, monster)
        if flag == 1:
            return (player_HP, player_gold, inventory, equipped, False)
        player_gold = monster_fight_HP(monster_HP, player_HP, player_gold)
        check = check_game_over(player_HP, player_gold)
        if check:
            exit()
    return (player_HP, player_gold, inventory, equipped, True)


#-------------------------Sleep / Game Over-------------------------#
'''Call sleep function to restore player HP.'''
def sleep(player_gold, player_HP):
    '''This function is used to let the player sleep and return to full HP.
    The cost of this is 5 Gold.
    If the player can't afford to sleep, they won't be able to.

    Arguments:
    player_gold, player_HP

    Return.
    player_HP, player_gold

    '''

    if player_gold >= 5:
        player_HP = 30
        player_gold -= 5
        print()
        print(f'/-----------------------------------------------\\')
        print(f'|                                               |')
        print(f'|    You slept and restored your HP to full!    |')
        print(f'|                                               |')
        print(f'\\-----------------------------------------------/')
        return (player_HP, player_gold)
    else:
        print()
        print(f'/-----------------------------------------------\\')
        print(f'|                                               |')
        print(f'|     You do not have enough Gold to sleep.     |')
        print(f'|                                               |')
        print(f'\\-----------------------------------------------/')

    check = check_game_over(player_HP, player_gold)
    if check:
        exit()


'''Call this function to check if the game is over. HP and Gold == 0.'''
def check_game_over(player_HP, player_gold):
    '''This function checks to see if the player has zero gold and zero HP.
    If so, the game will end.

    Arguments:
    player_HP, player_gold

    Return:
    None.

    '''

    if player_HP <= 0 and player_gold <= 0:
        print(f'/--------------------------------------------\\')
        print(f'|                                            |')
        print(f'|     You have no HP and no Gold left...     |')
        print(f'|                                            |')
        print(f'|                GAME OVER                   |')
        print(f'|                                            |')
        print(f'\\--------------------------------------------/')
        return True
    return False


#-------------------------Inventory-------------------------#
'''Call this function to view the shop inventory.'''
def shop_menu(items):
    '''This function displays a sign with the curent shop inventory.
    
    Arguments:
    items: list of available shop items.

    Return:
    None.

    '''
    
    print(f'/---------------------------------------------------------\\')
    print(f"| {'   ':<3}{'Item':<20}{'Item Type':<20}{'Cost':>10}{'   ':>1}|")
    print(f'|*********************************************************|')
    for index, item in enumerate(items):
        print(f"| {index+1:<1}) {item['name']:<20}{item['item type']:<20}{item['price']:>7} Gold |")
    print(f'|                                                         |')
    print(f'| * Magic Scrolls have a single use, instant kill effect. |')
    print(f'|                                                         |')
    print(f'| 6) Exit the shop                                        |')
    print(f'\\---------------------------------------------------------/')


'''Call this function to visit the shop and purchase an item.'''
def visit_shop(player_gold, inventory, equipped):
    '''This function allows the player to purchase an item for Gold.
    
    Arguments:
    player_gold, inventory

    Return:
    player_gold, inventory

    '''
    items = [
        {'name': 'Sword', 'item type': 'Weapon', 'damage': 5, 'max_durability': 25, 'amount': 1, 'current_durability': 25, 'price': 8}, 
        {'name': 'Shield', 'item type': 'Armor', 'reduction': 5, 'max_durability': 25, 'amount': 1, 'current_durability': 25, 'price': 6},
        {'name': 'Health Potion', 'item type': 'Consumable', 'effect': {'player_HP': 20}, 'amount': 1, 'price': 7},
        {'name': 'Poison Arrow', 'item type': 'Consumable', 'effect': {'monster_HP': 30}, 'amount': 1, 'price': 15},
        {'name': 'Magic Scroll', 'item type': 'Consumable', 'effect': 'instant kill', 'amount': 1, 'price': 20}
    ]
    shop_menu(items)
    shop_input = input("Please choose an item you'd like to purchase: ")

    if shop_input in ['1', '2', '3', '4', '5']:
        item = items[int(shop_input) - 1]
        owned_items = inventory + equipped
        if item['item type'] != 'Consumable':
            for owned in owned_items:
                if owned['name'] == item['name']:
                    print(f'/-------------------------------------------------\\')
                    print(f'|                                                 |')
                    print(f'|{f"You already own a {item['name']}!":^49}|')
                    print(f'|    You cannot own more than one of this item.   |')
                    print(f'|                                                 |')
                    print(f'\\-------------------------------------------------/')
                    return player_gold, inventory

        if player_gold >= item['price']:
            if item['item type'] == 'Consumable':
                found = False
                for inv_item in inventory:
                    if inv_item['name'] == item['name']:
                        inv_item['amount'] += 1
                        found = True
                        break
                if not found:
                    inventory.append(item)
            else:
                inventory.append(item)
            player_gold -= item['price']
            print(f'/----------------------------------------------------------\\')
            print(f'|                                                          |')
            print(f'|{f"You purchased a {item['name']} for {item['price']} Gold!":^58}|')
            print(f'|                                                          |')
            print(f'\\----------------------------------------------------------/')
        else:
            print(f'/-----------------------------------------------------------\\')
            print(f'|                                                           |')
            print(f'|{f"You do not have enough Gold to purchase a {item['name']}.":^59}|')
            print(f'|                                                           |')
            print(f'\\-----------------------------------------------------------/')
    elif shop_input == '6':
        print(f'/------------------------------------------------\\')
        print(f'|                                                |')
        print(f'|             You have left the shop.            |')
        print(f'|                                                |')
        print(f'\\------------------------------------------------/')

    else:
        print_invalid_input()

    return player_gold, inventory 


'''Call this function to manage player inventory.'''
def manage_inventory(inventory, equipped):
    '''This function is used to manage player inventory and equippable items.
    
    Arguments:
    inventory, equipped

    Return:
    inventory, equipped

    '''
    while True:
        valid_inventory = [item for item in inventory if item['item type'] != 'Consumable']
        inventory_menu(inventory, equipped, valid_inventory)
        equip_input = input("Select an item to de/equip, or type 'q' to exit the inventory: ")
        if equip_input == 'q':
            break
        if not equip_input.isdigit():
            print_invalid_input()
            continue
        equip_input = int(equip_input)
        if equip_input > len(valid_inventory + equipped):
            print_invalid_input()
            continue
        if equip_input > len(valid_inventory):
            item = equipped[equip_input - len(valid_inventory) - 1]
            equipped.pop(equip_input - len(valid_inventory) - 1)
            inventory.append(item)
        else:
            item = valid_inventory[equip_input - 1]
            inventory.pop(inventory.index(item))
            equipped.append(item)


    return inventory, equipped


'''Call this function to display player inventory.'''
def inventory_menu(inventory, equipped, equippable):
    '''This function is used to display player inventory and equip items.
    
    Arguments:
    inventory, equipped, equippable

    Return:
    None.

    '''
    print(f'/------------------------------------------------\\')
    print(f'|                PLAYER INVENTORY                |')
    print(f'|                ----------------                |')
    print(f'| {'Item':<16}  {'Item Type':<15}  {'Amount':<11} |')
    print(f'|************************************************|')
    for i, item in enumerate(inventory, start = 1): 
        print(f'| {item['name']:<18}{item['item type']:<17}{item['amount']:<12}|')
    print(f'|                                                |')
    print(f'\\------------------------------------------------/')

    print(f'/------------------------------------------------\\')
    print(f'|                   EQUIPPABLE                   |')
    print(f'|                ----------------                |')
    print(f'| {'   ':<3}{'Item':<15}{'Item Type':<17}{'Durability':<10}  |')
    print(f'|************************************************|')
    for i, item in enumerate(equippable, start = 1):
        print(f'| {i}) {item['name']:<15}{item['item type']:<17}{f"{item['current_durability']}/{item['max_durability']}":<10}  |')
    print(f'|                                                |')
    print(f'\\------------------------------------------------/')
    
    print(f'/------------------------------------------------\\')
    print(f'|                    EQUIPPED                    |')
    print(f'|                ----------------                |')
    print(f'| {'   ':<3}{'Item':<15}{'Item Type':<17}{'Durability':<10}  |')
    print(f'|************************************************|')
    for i, item in enumerate(equipped, start = len(equippable)+1):
        print(f'| {i}) {item['name']:<15}{item['item type']:<17}{f"{item['current_durability']}/{item['max_durability']}":<10}  |')
    print(f'|                                                |')
    print(f'\\------------------------------------------------/')


#-------------------------Invalid Input-------------------------#
'''Call this function to display 'Invalid Input'.'''
def print_invalid_input():
    '''This function is called to display an 'Invalid Input' message.
    
    Arguments:
    None

    Return:
    None

    '''

    print(f'/------------------------------------------------\\')
    print(f'|                                                |')
    print(f'| Invalid input. Please enter a valid selection. |')
    print(f'|                                                |')
    print(f'\\------------------------------------------------/')



#-------------------------Save Game-------------------------#

'''Call this function to save player data.'''
def save_game(player_HP, player_gold, inventory, equipped, map):
    '''This function saves player data.
    
    Arguments:
    player_HP, player_gold, inventory, equipped

    Return:
    None.

    '''
    serialized_map = {
        "player_position": map["player_position"],
        "town_position": map["town_position"],
        "monsters": []    
    }
    for monster in map["monsters"]:
        serialized_map["monsters"].append(monster.serialize())
    player_data = {
        "player_hp": player_HP,
        "player_gold": player_gold,
        "inventory": inventory,
        "equipped": equipped,
        "map": serialized_map
    }
    with open('save.json', 'w') as player_save:
        json.dump(player_data, player_save, indent=4)


'''Call this function to load saved player data.'''
def load_game():
    '''This function loads saved player data.
    
    Arguments:
    None.

    Return:
    player_data

    '''
    with open('save.json', 'r') as player_save:
        player_data = json.load(player_save)

    for i, monster_dict in enumerate(player_data["map"]["monsters"]):
        monster = wanderingMonster.Monster()
        player_data["map"]["monsters"][i] = monster.deserialize(monster_dict)
    return player_data


#-------------------------Graphics-------------------------#
'''Call this function to explore the map.'''
def explore(player_HP, player_gold, inventory, equipped, map_state):
    '''This function is called to explore the map and search for monsters.
    
    Arguments:
    player_HP, player_gold, inventory, equipped

    Return:
    player_HP, player_gold, inventory, equipped

    '''
    # if len(map_state["monsters"]) <= 0 :
    #     map_state = map_module.respawn_monsters(map_state)

    while True:
        result, monster = map_module.show_map(map_state)

        if result == "battle":

            player_HP, player_gold, inventory, equipped, monster_defeated_flag = fight_monster(player_HP, player_gold, inventory, equipped, monster)

            if not monster_defeated_flag:
                print(f'/---------------------------------------------\\')
                print(f'|                                             |')
                print(f'|        You ran away from the fight.         |')
                print(f'|        Head back to town to heal up!        |')
                print(f'|                                             |')
                print(f'\\---------------------------------------------/')
                continue
                # return player_HP, player_gold, inventory, equipped, map_state

            if player_HP > 0:
                
                map_state["monsters"].remove(monster)

                print(f'/---------------------------------------------\\')
                print(f'|                                             |')
                print(f'|   You returned to the map after the fight.  |')
                print(f'|                                             |')
                print(f'\\---------------------------------------------/')

                continue

                # return player_HP, player_gold, inventory, equipped, map_state
            
            else:
                #Player died during the fight.
                map_state["player_position"] = map_state["town_position"]
                break

        elif result == "town":
            print(f'/---------------------------------------------\\')
            print(f'|                                             |')
            print(f'|     You returned to town. Welcome back!     |')
            print(f'|                                             |')
            print(f'\\---------------------------------------------/')
            break

    return player_HP, player_gold, inventory, equipped, map_state


