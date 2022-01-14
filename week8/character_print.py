# character print exercise

def character_print(num, name):
    print("\nNumber: {} and Name: {}" .format(num, name))
    for line in range(num):
        print(name, end="\n")


number = int(input("\nType x times to print the character: "))
character = str(input("Type the character name to print: "))
character_print(number, character)

# Functions:
# def name(parameter):
# def formatrow(header=False) = default value parameter
# id() : give id in memory
# len(): length of the data sequence or collection
# reversed(): print reversed items
# sorted(): print sorted items
# filter(): filter elements
# map(): (function, iterable) - will go through every item on the iterable
# open(): open file object

fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
fullname("    leonard", "EULER")
print(fullname)
