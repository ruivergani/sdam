# restaurant exercise
print("\n1: Lasagne | 2: Stir Fry")
order = int(input("\nType your order number: "))

if order == 1:
    second_dish = int(input("\n1: Garlic Bread | 2: Fries: "))
    if second_dish == 1:
        print("\nOrder: Lasagne with Garlic Bread")
    elif second_dish == 2:
        print("\nOrder: Lasagne with Fries")
    else:
        print("Invalid Selection.")
elif order == 2:
    second_dish = int(input("1: Noodles | 2: Crispy Seaweed: "))
    if second_dish == 1:
        print("\nOrder: Stir Fry with Noodles")
    elif second_dish == 2:
        print("\nOrder: Stir Fry with Crispy Seaweed")
    else:
        print("Invalid Selection.")
else:
    print("Invalid number dish selection. ")
