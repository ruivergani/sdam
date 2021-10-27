# program to calculate coin_toss

import math
import random

# simulate coin toss randomly
coin_toss = random.randint(0, 1)

if coin_toss == 1:
    coin_toss_result = "Heads"
    print("\nSorted: Heads")
else:
    coin_toss_result = "Tails"
    print("\nSorted: Tails")

user_guess = input("Please type your guess: ")

if user_guess == coin_toss_result:
    print("You guessed correctly")
else:
    print("You guessed incorrectly")


# the main issue with this algorithm is that there is no validation at all and just simple uppercase letter or
# type error will provide user wrong output
