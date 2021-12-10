# Handling Exceptions

guess = 0

while not(0 < guess < 6):
    try:
        guess = int(input("Enter an integer: "))
        if not (0 < guess < 6): raise Exception
    except ValueError:
        print("Requires an integer type.")
    except Exception:
        print("Requires an integer between 1 and 5.")

#  ZeroDivisionError: dividend is zero
#  IndexError: index length out of range
#  KeyError: dictionary key not found
#  FileNotFoundError: file not found
#  TypeError: wrong type operation
#  ValueError: correct type wrong

try:
    value = 10 / 0
    number = int(input("Type a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by zero.")
except ValueError:
    print("Invalid input.")