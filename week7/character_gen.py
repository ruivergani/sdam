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

# print the character table minimum ability table
x = PrettyTable()
x.field_names = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
x.add_row(["Warrior", 15, "-", "-", 12, 10])
x.add_row(["Wizard", "-", 15, 10, 10, "-"])
x.add_row(["Thief", 10, 9, "-", 15, "-"])
x.add_row(["Necromancer", 10, 10, 15, "-", "-"])

print(x)
