# high_low exercise (Not completed)

import math
import random

# Generate card
card = int(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # fix the string issue regarding the list (how can you compare the string ace, queen...
print("\nRandom First Card: {}" .format(card))

# Get user guess
user_guess = str(input("\nNext card will be higher or lower? (< >): "))

temp = 0
# Compare user guess
if user_guess == ">":
    print("You guessed will be higher.")
    temp = 1
elif user_guess == "<":
    print("You guessed lower.")
    temp = 0
else:
    print("Wrong data input.")

# Generate second card
card2 = int(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print("\nRandom Second Card: {}" .format(card2))

# Compare index (position of the array) of the second card with first card
if card2 > card:
    print("\nDeal: ")
    print("Second card is higher.")
    if temp == 1:
        print("You guessed correctly. You won!")
    else:
        print("Wrong guess. You lost!")
else:
    print("\nDeal: ")
    print("Second card is lower.")
    if temp == 0:
        print("You guessed correctly. You won! ")
    else:
        print("Wrong guess. You lost!")