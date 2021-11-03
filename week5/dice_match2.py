# dice_match

import math
import random

dice = int(random.randint(1, 6))

# calculations to match the dices
counter = 0  # how mane throws before matched

while dice != 7:
    dice1 = int(random.randint(1, 6))
    dice2 = int(random.randint(1, 6))
    print("Dice 1: {}".format(dice1))
    print("Dice 2: {}".format(dice2))
    print("")
    counter = counter + 1
    if dice1 == dice2:
        print("\nMatching pair: {} {} " .format(dice1, dice2))
        throws = counter
        print("Throws: {} " .format(throws))
        dice = 7
        break
    else:
        continue

print("\nEnd of program.")