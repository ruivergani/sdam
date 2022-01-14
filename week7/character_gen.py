# character gen (DONE)

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
        new_char = ["Warrior", 15, 0, 0, 12, 10]
    elif c_chosen == 2:
        new_char = ["Wizard", 0, 15, 10, 10, 0]
    elif c_chosen == 3:
        new_char = ["Thief", 10, 9, 0, 15, 0]
    else:
        new_char = ["Necromancer", 10, 10, 15, 0, 0]
except ValueError:
    print("Requires an integer option.")

print("\nYour new character table generator: ")
# print the character generator
y = PrettyTable()
y.field_names = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
y.add_row(["Base Score", strength, intelligence, wisdom, dexterity, constitution])
sum_random_char = int(strength + intelligence + wisdom + dexterity + constitution)
y.add_row([new_char[0], new_char[1], new_char[2], new_char[3], new_char[4], new_char[5]])
# calculate points to exchange
deficit = ["Deficit/Surplus", (strength - new_char[1]), (intelligence - new_char[2]), (wisdom - new_char[3]), (dexterity - new_char[4]), (constitution - new_char[5]) ]
y.add_row(["Deficit/Surplus", deficit[1], deficit[2], deficit[3], deficit[4], deficit[5]])
print(y)

#  redistribution of attributes (only once)
print("\n1: Strength | 2: Intelligence | 3: Wisdom | 4: Dexterity | 5: Constitution")
attribute_sacrifice = int(input("\nWhich attributes you want to sacrifice? "))
if (deficit[attribute_sacrifice]) < 0:
    print("You can't sacrifice this attribute.")
    exit
else:
    points_exchange = int(input("How many points you want to exchange?: "))
    attribute_assign = int(input("Assign to where? (number): "))
    deficit[attribute_assign] = (deficit[attribute_assign] + points_exchange)
    print("\nNew value of attribute assigned: ", deficit[attribute_assign])
    deficit[attribute_sacrifice] = deficit[attribute_sacrifice] - points_exchange
    print("Attribute Sacrificed has now: ", deficit[attribute_sacrifice])

# Dictionaries
# months = {"Jan":31, "Feb":28}
# months['Feb']=28
# .keys() | .values() | .items()
# thisdic.update({"March": 30})
# thisdic.pop("model") or .popitem() or del thisdic or del thisdic["model"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[6:2:-2])
['mango', 'kiwi']

# Negative indexing means starting from the end of the list.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1,



