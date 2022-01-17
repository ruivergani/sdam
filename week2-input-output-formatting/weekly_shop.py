# weekly_shop intermediate algorithm

print("\nPeaches:")
peaches = int(input("- How many? "))
peaches_price = float(input("- Price? £"))

print("\nBeans:")
beans = int(input("- How many? "))
beans_price = float(input("- Price? £"))

print("\nChicken Pieces:")
chicken = int(input("- How many? "))
chicken_price = float(input("- Price? £"))

print("\nSocks:")
socks = int(input("- How many? "))
socks_price = float(input("- Price? £"))

print("\nBottle of water:")
bottle_water = int(input("- How many? "))
bottle_water_price = float(input("- Price? £"))

# calculations:

total_items = (peaches + beans + chicken + socks + bottle_water)
weekly_cost = float(((peaches_price * peaches) + (beans_price * beans) + (chicken_price * chicken) + (socks_price * socks) + (bottle_water_price * bottle_water)))

print("\nTotal number of items purchased: {} " .format(total_items))
print("Your weekly shop cost: {:.2f} £" .format(weekly_cost))

print("\nTake your receipt.")