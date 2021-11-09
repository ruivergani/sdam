# pairs exercise

import math
import random

print("\nWelcome to the pairs exercise.\n")

# card face up
card_face_up = [["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"]]
j = 0
print("Face Up: ")
print("   0    1     2    3")
for i in range(len(card_face_up)):
    print(i, end=" ", sep=" ")
    for j in range(len(card_face_up[i])):
        print(card_face_up[i][j], end=" ")
    print()

# card face down
print("\nFace Down: ")
print("   0   1   2   3")
for i in range(len(card_face_up)):
    print(i, end=" ", sep=" ")
    for j in range(len(card_face_up[i])):
        print(" * ", end=" ")
    print()

# request from user
row = int(input("\nEnter a card position (row): "))
column = int(input("Enter a card position (column): "))
# access an index (first card)
print("\nFirst Card chosen: ", card_face_up[row][column])

x = int(input("\nEnter second card to compare: (row)"))
y = int(input("Enter second card to compare: (column)"))
# access an index (second card)
print("\nSecond Card chosen: ", card_face_up[x][y])

while card_face_up[row][column] != card_face_up[x][y]:
    print("\nNo match found.")
    # request from user
    row = int(input("\nEnter a card position (row): "))
    column = int(input("Enter a card position (column): "))
    # access an index (first card)
    print("\nFirst Card chosen: ", card_face_up[row][column])
    x = int(input("\nEnter second card to compare: (row)"))
    y = int(input("Enter second card to compare: (column)"))
    # access an index (second card)
    print("\nSecond Card chosen: ", card_face_up[x][y])
else:
    print("You have matched values. ")
    j = 0
    card_face_up[row][column] = "X"
    card_face_up[x][y] = "X"
    print("\nNew layout: ")
    print("   0    1     2    3")
    for i in range(len(card_face_up)):
        print(i, end=" ", sep=" ")
        for j in range(len(card_face_up[i])):
            print(card_face_up[i][j], end=" ")
        print()