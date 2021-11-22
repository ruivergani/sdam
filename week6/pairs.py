# pairs exercise

import math
import random

print("\nWelcome to the pairs exercise.\n")

card_face_up = [["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"]]

card_face_down = [[" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "]]

game_over = [[" X ", " X ", " X ", " X "],
             [" X ", " X ", " X ", " X "],
             [" X ", " X ", " X ", " X "],
             [" X ", " X ", " X ", " X "]]

# display both set of cards
j = 0
print("Face Up: ")
print("   0    1     2    3")
for i in range(len(card_face_up)):
    print(i, end=" ", sep=" ")
    for j in range(len(card_face_up[i])):
        print(card_face_up[i][j], end=" ")
    print()
print("\nFace Down: ")
print("   0   1   2   3")
for i in range(len(card_face_down)):
    print(i, end=" ", sep=" ")
    for j in range(len(card_face_down[i])):
        print(card_face_down[i][j], end=" ")
    print()

while card_face_up != game_over:
    # display user input (no validation)
    row = int(input("\nEnter a card position (row): "))
    column = int(input("Enter a card position (column): "))
    print("\nFirst Card chosen: ", card_face_up[row][column])
    x = int(input("\nEnter second card to compare (row): "))
    y = int(input("Enter second card to compare (column): "))
    print("\nSecond Card chosen: ", card_face_up[x][y])

    while card_face_up[row][column] != card_face_up[x][y]:
        print("\nNo match found.")

        # display user input (no validation)
        row = int(input("\nEnter a card position (row): "))
        column = int(input("Enter a card position (column): "))
        print("\nFirst Card chosen: ", card_face_up[row][column])
        x = int(input("\nEnter second card to compare (row): "))
        y = int(input("Enter second card to compare (column): "))
        print("\nSecond Card chosen: ", card_face_up[x][y])
    else:
        print("You have matched values. ")
        j = 0
        card_face_up[row][column] = " X "
        card_face_up[x][y] = " X "
        print("\nNew layout: ")
        print("  0   1    2   3")
        for i in range(len(card_face_up)):
            print(i, end=" ", sep=" ")
            for j in range(len(card_face_up[i])):
                print(card_face_up[i][j], end=" ")
            print()