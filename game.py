#CSCI 150 Assignment 7 - Adventure Module (Project)
#Rebecca Jaquith
#March 9, 2025

'''In this module I will import the gamefunctions.py file and call the 4 required functions.
The 4 required functions are purchase_item(), new_random_monster(),
print_welcome(), and print_shop_menu().
'''

#Import the gamefunctions module.
import gamefunctions

#Demonstration of basic user interaction.
user_input = input('Enter your name:')

#Call each of the 4 required functions once.

#Call Function 1 using an example from gamefunctions.py.
from gamefunctions import purchase_item

num_purchased, leftover_money = purchase_item(1.23, 10, 3)

print(num_purchased)
print(leftover_money)


#Call Function 2 using an example from gamefunctions.py.
from gamefunctions import new_random_monster

my_monster = new_random_monster()

print(my_monster['name'])
print(my_monster['description'])
print(my_monster['health'])
print(my_monster['power'])
print(my_monster['money'])


#Call Function 3 using an example from gamefunctions.py.
gamefunctions.print_welcome("Becca")


#Call Function 4 using an example from gamefunctions.py.
gamefunctions.print_shop_menu("Apple", 31, "Pear", 1.234)


