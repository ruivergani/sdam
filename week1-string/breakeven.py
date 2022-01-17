# breakeven exercise

import math

item_price = float(20)
print("Cost to produce each item: £" + str(item_price))

sale_price = float(40)  # item cost + profit per item
print("Sale price for each item: £" + str(sale_price))

# week 1
# P E M D A S = () ** * / + - print(2 ** 3 ** 2) = right-left
# // floor division (int value)
# / (float division)
# % rest of division
# / = type special character | '' or "" or """ """ as long is consistent
# print(sep=''  separate objects, end='\n' default new line, file=sys.stdout sent to default stdout, flush=False force buffer)
# snake case = name_variable

fixed_costs = float(50000)
print("Fixed costs: £" + str(fixed_costs))

item_profit = float((sale_price - item_price))
print("Profit per item: £" + str(item_profit))

breakeven = (fixed_costs / item_profit)
print("Breakeven: " + str(breakeven) + " items")


# str() int() float() bool()
