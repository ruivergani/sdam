# cost of living algorithm

print("\n === Welcome to the program ===")

rent = float(input("\nRent per month: "))
gas = float(input("Gas payment per month: "))
electricity = float(input("Electricity payment per month: "))
water = float(input("Water payment per month: "))
council_tax = float(input("Council tax payment per month: "))

total_sum = (rent + gas + electricity + water + council_tax)

print("\nYour monthly expenses are: ")
print("{:<20}£{:>6.2f}" .format("Rent:", rent))
print("{:<20}£{:>6.2f}" .format("Gas:", gas))
print("{:<20}£{:>6.2f}" .format("Electricity:", electricity))
print("{:<20}£{:>6.2f}" .format("Water:", water))
print("{:<20}£{:>6.2f}" .format("Council Tax:", council_tax))
print("="*28)
print("{:<20}£{:>6.2f}" .format("Total:", total_sum))