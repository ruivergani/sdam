# breakeven exercise

import math

item_price = float(20)
print("Cost to produce each item: £" + str(item_price))

sale_price = float(40)  # item cost + profit per item
print("Sale price for each item: £" + str(sale_price))

fixed_costs = float(50000)
print("Fixed costs: £" + str(fixed_costs))

item_profit = float((sale_price - item_price))
print("Profit per item: £" + str(item_profit))

breakeven = (fixed_costs / item_profit)
print("Breakeven: " + str(breakeven) + " items")
