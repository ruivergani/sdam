# dice_match

import math
import random

print("\nDice match algorithm.")

# calculations to match the dices
counter = 1  # how mane throws before matched

dice1 = int(random.randint(1, 6))
dice2 = int(random.randint(1, 6))
if(dice1 == dice2):
    print("\nDice matched at first throw. ")
    print("Matching pair: {} {}" .format(dice1, dice2))
else:
    print("\nDice has not matched at first throw.")

while dice1 != 6:
    dice1 = int(random.randint(1, 6))
    dice2 = int(random.randint(1, 6))
    print("Dice 1: {}".format(dice1))
    print("Dice 2: {}".format(dice2))
    print("")
    counter = counter + 1
    if dice1 == dice2:
        print("\nMatching pair: {} {} " .format(dice1, dice2))
        print("Throws: {} " .format(counter))
        break
    else:
        continue

print("\nEnd of program.")