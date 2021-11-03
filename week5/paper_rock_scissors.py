# exercise paper_rock_scissors

import math
import random

print("\nRock / Paper / Scissors ")
score_user = 0
score_computer = 0

while (score_user < 3) or (score_computer < 3):
    # user choice
    user_choice = input("\nEnter your selection: ").strip().lower()
    print("You chose: {}".format(user_choice))

    # computer choice generated randomly
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("The computer chose: {}".format(computer_choice))

    # variables for message
    computer_wins = "The computer won!"
    you_win = "Congratulations, you win!"

    # computer wins
    if (user_choice == 'scissors' and computer_choice == 'rock') or \
            (user_choice == 'paper' and computer_choice == 'scissors') or \
            (user_choice == 'rock' and computer_choice == 'paper'):
        print(computer_wins)
        score_computer += 1
        print("Computer score is: {}".format(score_computer))

    # user wins
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        print(you_win)
        score_user += 1
        print("Your score is: {}".format(score_user))
    else:
        if user_choice == computer_choice:
            print("It's a draw.")
            score_user += 0
            score_computer += 0
        else:
            continue
print("Game over.")