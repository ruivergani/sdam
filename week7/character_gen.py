# character gen (NOT FINISHED YET)

import random
import math
from prettytable import PrettyTable
from tabulate import tabulate

character = ["Warrior", "Wizard", "Thief", "Necromancer"]

# character attributes
strength = int(random.randint(3, 18))
intelligence = int(random.randint(3, 18))
wisdom = int(random.randint(3, 18))
dexterity = int(random.randint(3, 18))
constitution = int(random.randint(3, 18))

warrior = ["Warrior", 15, "-", "-", 12, 10]
wizard = ["Wizard", "-", 15, 10, 10, "-"]
thief = ["Thief", 10, 9, "-", 15, "-"]
necromancer = ["Necromancer", 10, 10, 15, "-", "-"]

# print the character table minimum ability table
x = PrettyTable()
x.field_names = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
x.add_row(["Warrior", 15, "-", "-", 12, 10])
x.add_row(["Wizard", "-", 15, 10, 10, "-"])
x.add_row(["Thief", 10, 9, "-", 15, "-"])
x.add_row(["Necromancer", 10, 10, 15, "-", "-"])
print(x)

# try and catch exception to get
try:
    print("\n1: Warrior")
    print("2: Wizard")
    print("3: Thief")
    print("4: Necromancer")
    c_chosen = int(input("\nWhich character number you want to be? "))
    if c_chosen == 1:
        new_char = ["Warrior", 15, "-", "-", 12, 10]
    elif c_chosen == 2:
        new_char = ["Wizard", "-", 15, 10, 10, "-"]
    elif c_chosen == 3:
        new_char = ["Thief", 10, 9, "-", 15, "-"]
    else:
        new_char = ["Necromancer", 10, 10, 15, "-", "-"]
except ValueError:
    print("Requires an integer option.")

print("\nYour new character table generator: ")
# print the character generator
y = PrettyTable()
y.field_names = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
y.add_row(["Base Score", strength, intelligence, wisdom, dexterity, constitution])
sum_random_char = int(strength + intelligence + wisdom + dexterity + constitution)
y.add_row([new_char[0], new_char[1], new_char[2], new_char[3], new_char[4], new_char[5]])
y.add_row("Amended Score", "-", "-", "-", "-", "-")
print(y)

#  redistribution of attributes
attribute_sacrifice = input("Which attributes you want to sacrifice? ")
points_exchange = input("How many points you want to exchange? ")
attribute_assign = input("1: Strength | 2: Intelligence | 3: Wisdom | 4: Dexterity | 5: Constitution ? ")

