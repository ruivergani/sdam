# sales

number = int(input("\nType your amount: "))

if number < 999:
    discount = (number * 0.1)
    result = number - discount
elif number > 999:
    discount = (number * 0.2)
    result = number - discount

print("Net amount: £{}" .format(result))