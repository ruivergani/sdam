# reverse array output example

import math
import random

thislist = []
counter = 1
while counter < 6:
    number = int(input("\nPlease enter " + str(counter) + " list: "))
    thislist.append(number)  # add number to the list
    counter += 1

print("\nNormal: ", thislist)
thislist.reverse()
print("\nReversed: ", thislist)