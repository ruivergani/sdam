# character print exercise

def character_print(num, name):
    print("\nNumber: {} and Name: {}" .format(num, name))
    for line in range(num):
        print(name, end="\n")


number = int(input("\nType x times to print the character: "))
character = str(input("Type the character name to print: "))
character_print(number, character)
