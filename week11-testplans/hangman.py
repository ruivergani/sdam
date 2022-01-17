# simplified version of hangman

import sys
import random


def hangman():
    wordbank = ["avocado", "chicken", "funds", "bankrupt", "cushion", "filming", "apartment", "radio", "detective",
                "vinegar", "curtains", "carpet", "addictive", "control", "raining", "sunshine", "diamond", "charcoal",
                "chocolate", "container", "cubes", "fan", "processor", "sunbed", "towel", "jellyfish", "meals"]
    word = random.choice(wordbank)
    guesses = " "
    turns = 1
    while turns > 0:
        failed = 0
        print("\nWord: ")
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print(" - ", end=' ')
                failed += 1
        if failed == 0:
            print("\nYou win!")
            print("It took you ", turns, " guesses to finish.")
            exit()
        # guess code character
        print()
        guess = input("\nGuess a character: ")
        guesses += guess
        if guess not in word:
            turns += 1
            print("Wrong!")
        else:
            turns += 1
            print("Correct guess.")
hangman()
