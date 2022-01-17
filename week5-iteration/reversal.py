# exercise reversal

number = str(input("\nEnter an integer (1-11 digits) or -1 to exit: "))

while number != '-1':
    if (len(str(number)) > 1) and (len(str(number)) < 11):
        print("Length of number: {}".format(len(str(number))))  # length of the number
        print("Reverse: ", (number[::-1]))
        number = str(input("\nEnter an integer (1-11 digits) or -1 to exit: "))
    else:
        print("Invalid input.")
        number = str(input("\nEnter an integer (1-11 digits) or -1 to exit: "))
else:
    print("You exited.")