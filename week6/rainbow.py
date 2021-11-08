# exercise beginner
# store color of rainbow
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# user (-1 to stop) (1-7)
print("\n(1-7) Type any out of range number to exit.")
num = int(input("Enter an integer (1-7): "))
while (num >= 1) and (num <= 7):
    if num == 1:
        chosen_value = rainbow[0]
    elif num == 2:
        chosen_value = rainbow[1]
    elif num == 3:
        chosen_value = rainbow[2]
    elif num == 4:
        chosen_value = rainbow[3]
    elif num == 5:
        chosen_value = rainbow[4]
    elif num == 6:
        chosen_value = rainbow[5]
    else:
        chosen_value = rainbow[6]
    print("You picked: {}" .format(chosen_value))
    num = int(input("\nEnter an integer (1-7): "))
else:
    print("\nOut of range! Exit program.")
