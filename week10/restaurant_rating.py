import random
import math
from prettytable import PrettyTable
from tabulate import tabulate

print("\n----- Rate the restaurant -------")
print("-1: exit")
print("Range 1 - 5, where 1 is very poor and 5 is very good")
number = 0
vote = 0
counter = 0
rating = 0
n = 0
average = 0
# rating the restaurant
while counter != -1:
    try:
        vote = int(input("\nVote (1-5): "))
        if 1 < vote < 6:
            rating = (rating + vote)
            n += 1
        elif vote == -1:
            print("Exiting Program.")
            counter = -1
        else:
            raise Exception
    except ValueError:  # validate integer
        print("Requires an integer.")
    except Exception:  # validate range 1-5
            print("The value must be in the range 1-5")

average = (rating / n)
result = round(average, 2)
y = PrettyTable()
y.field_names = ["Vote Quantity", "Average"]
y.add_row([n, average])
print(y)

if result == 1:
    print("\nFinal rate is: Very Poor")
elif result == 2:
    print("\nFinal rate is: Poor")
elif result == 3:
    print("\nFinal rate is: Medium")
elif result == 4:
    print("\nFinal rate is: Good")
else:
    print("\nFinal rate is: Very Good")