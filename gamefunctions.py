#CSCI 150 Assignment 8 - Adventure Module (Project)
#Rebecca Jaquith
#March 9, 2025

#In this assignment I will be modifying the gamefunctions file so that it can be used as a module from another file and experimenting with importing it by game.py.
#The existing functions are purchase_item(), new_random_monster(), print_welcome(), and print_shop_menu().
#The new functions are test_functions() and main().

'''This module provides functions to be imported by the game.py file.

It includes six functions. 1 through 4 are the required game functions.
Function 1 is purchase_items() and is used to return the number of
items purchased and the amount of money remaining.
Function 2 is new_random_monster() and is used to return three random monsters 
and various properties associated with each monster.
Function 3 is print_welcome() and is used to print a welcome sign
for the supplied 'name' parameter.
Function 4 is print_shop_menu() and is used to print a sign that contains
a list of two items and their corresponding prices.
The fifth function down is called test_functions and is used to print
the output of Functions 1 through 4.
The sixth function is called main() and is used to test if the function is true
when gamefunctions is run.
'''

#Function 1 purchase_item().

'''Call the purchase_item() function to return the number of items purchased and the amount of money remaining.'''
import random

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int=1):
    '''Calculate the number of items purchased and the amount of money remaining.
    If there isn't enough money, adjust the quantity of items purchased.

    Arguments:
    itemPrice -- a floating integer parameter of how much the item costs.
    starting Money -- a floating integer parameter of how much money the user starts with.
    quantityToPurchase -- has a default parameter of 1 unless otherwise specified.

    Return:
    quantity purchased, amount of money remaining.

    '''
    #We need to calculate the total cost of the items.
    total_cost = itemPrice * quantityToPurchase
    #We need to figure out how much we can buy before we go over startingMoney?
    if startingMoney > total_cost:
        #If we have money left over:
        quantity_purchased = quantityToPurchase
        amount_money_remaining = startingMoney - total_cost
        
    else:
        #If we can only buy as many as can be afforded (not enough money):
        quantity_purchased = int(startingMoney // itemPrice)
        amount_money_remaining = startingMoney - quantity_purchased * itemPrice
          
    #Return the quantity purchased and the amount of money remaining.    
    return (quantity_purchased, amount_money_remaining)




#Function 2 new_random_monster()

'''Call the new_random_monster() function to return three random monsters and various properties associated with each monster.'''
def new_random_monster():
    '''Create character profiles for three different monsters.

    Arguments:
    None.

    Return:
    A dictionary that contains at least the following keys: name, description, health, power, money.

    '''
    #Need to create a random monster.
    #3 names (monster types).
    #Health, power, and money ranges, different for all 3 monster types.
    #Dictionary
    random_monster_types = [
        {
            'name': 'Goblin',
            'description': 'This goblin is green, five feet tall, and has a hump on there back.',
            'health': random.randint(8, 12),
            'power': random.randint(23, 27),
            'money': random.randint(1, 5)
        },
        {
            'name': 'Mummy',
            'description': 'This mummy is three thousand years old and lives with his mother.',
            'health': random.randint(13, 17),
            'power': random.randint(28, 32),
            'money': random.randint(101, 105)
        },
        {
            'name': 'Vampire',
            'description': 'This vampire is a real narcissist and can\'t stop looking in the mirror.',
            'health': random.randint(18, 22),
            'power': random.randint(33, 37),
            'money': random.randint(201, 205)
        }
    ]
    
    a_monster = random.choice(random_monster_types)

    #Return a random monster and its various properties using the dictionary.
    return a_monster




#Function 3 print_welcome()

'''Call the print_welcome() function to print a welcome sign for the supplied 'name' parameter.
The output is centered within a 20-character field.
'''
def print_welcome(name:str, width:int = 20):
    '''Prints a welcome message with a 'name' parameter.

    Arguments:
    name:str -- string representing a name parameter.
    width:int = 20 -- the width of the 20-character field.

    Return:
    None.

    '''
    #The message we need to output.
    welcome_message = (f'Hello, {name}!')

    #Center the message.
    centered_welcome_message = (f'{welcome_message:^20}')
    
    #Print the message centered within the width parameter.
    print(centered_welcome_message)




#Function 4 print_shop_menu()

'''Call the print_shop_menu() function to print a sign that contains a list of two items and their corresponding prices.'''
def print_shop_menu(item1Name:str, item1Price:float, item2Name:str, item2Price:float):
    '''Print a sign that contains a list of two items and their corresponding prices.
    Items are left-aligned in the menu, while the prices are right aligned (with decimal points lining up).
    Prices formatted to show 2 decimal points, and preceded with a dollar sign(no space between).
    Item name field has 12 characters, and item price field has 8 characters.
    Sign is surrounded by a border.

    Arguments:
    item1Name:str -- string representing an item name input.
    item1Price:float -- a float interger parameter with item1 price.
    item2Name:str -- string representing an item name input.
    item2Price:float -- a float interger parameter with item2 price.

    Return:
    None.

    '''
    #Print the top of the sign border.
    print(f'/----------------------\\')

    #Print the first item, price, and border.
    dollar_item1Price = (f'${item1Price:.2f}')
    print(f'| {item1Name:<12}{dollar_item1Price:>8} |')

    #Print the second item, price, and border.
    dollar_item2Price = (f'${item2Price:.2f}')
    print(f'| {item2Name:<12}{dollar_item2Price:>8} |')

    #Print the bottom of the border.
    print(f'\\----------------------/')
    



#Function test_functions().

'''Call test_functions to print the output of Functions 1 through 4.'''
def test_functions(): 
    '''Function test_functions contains the test code for Functions 1 through 4.

    Arguements: 
    None.

    Return:
    None.

    '''

    #Call Function 1 four times. I used the same number of calls and values as the example.
    #Run 1
    num_purchased, leftover_money = purchase_item(1.23, 10, 3)

    print(num_purchased)
    print(leftover_money)

    #Run 2
    num_purchased, leftover_money = purchase_item(1.23, 2.01, 3)

    print(num_purchased)
    print(leftover_money)

    #Run 3
    num_purchased, leftover_money = purchase_item(3.41, 21.12)

    print(num_purchased)
    print(leftover_money)

    #Run 4
    num_purchased, leftover_money = purchase_item(31.41, 21.12)

    print(num_purchased)
    print(leftover_money)


    #Call Function 2 three times.
    #Run 1
    my_monster = new_random_monster()

    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])

    #Run 2
    my_monster = new_random_monster()

    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])

    #Run 3
    my_monster = new_random_monster()

    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])


    #Call Function 3 three times.
    #Run 1
    print_welcome("Becca")

    #Run 2
    print_welcome("Miranda")

    #Run 3
    print_welcome("Rachel")


    #Call Function 4 three times. I used the same values as the example.
    #Run 1
    print_shop_menu("Apple", 31, "Pear", 1.234)

    #Run 2
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
                    
    #Run 3
    print_shop_menu("Cheese", 6.78, "Sandwich", 5.43)


#Function main().

'''Used to test if statement is true, if test_fuctions() is called.'''
def main():
    '''This function calls the function test_function().

    Arguments:
    None.

    Return:
    None.
    '''

    #Call test_functions.
    test_functions()

if __name__ == "__main__":
    main()






