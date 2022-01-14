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

# week 4
# Selection (IF STATEMENT) = if elif else
# not(x>y) result is False (x = 4 and y = 3) (will always be the opposite)
# Logical and Operational Operators

# Lists: mylist=["apple", "banana"] (different data type, multiple values, allow duplicate, changeable)
# Tuples: mytuple=("apple", "banana") (store in a single variable, unchangeable)
# Sets: thisset={"apple", "banana"} (unordered, unchangeable, no index, no duplicate items)
# Dictionary: data in key:value pairs, thisdic={"brand":"ford"} | mutable | using keys index | no duplicate | ordered
