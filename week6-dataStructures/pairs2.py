# pairs exercise

import math
import random

print("\nWelcome to the pairs exercise.\n")

# card face up
card_face_up = [["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"],
                ["Jack", "King", "Ace", "Queen"]]

card_face_down = [[" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "],
                  [" * ", " * ", " * ", " * "]]
# card face up
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
for i in range(len(card_face_down)):
    print(i, end=" ", sep=" ")
    for j in range(len(card_face_down[i])):
        print(card_face_down[i][j], end=" ")
    print()

