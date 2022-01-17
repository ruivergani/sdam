# theatre (exercise)
# color packet (just to change the output console)
CEND = '\33[0m'

CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'

print(CBLUE + "\n=== Welcome to the theatre ticket service! ===")

adult = float(10.50)
child = float(7.30)
concessions = float(8.40)  # > 65 years old

# print ticket information
print("{:<15} {:<15}".format('\nTicket', 'Stalls'))
print("_____________________")
print("{:<15} £{:<15}".format('Adult', adult))
print("{:<15} £{:<15}".format('Child', child))
print("{:<15} £{:<15}".format('Concessions', concessions) + CEND)

# inform user ticket requirements
print(CGREEN + "\nConcessions are available for adults over the age of 65. ")
print("All children must be accompanied by at least one adult." + CEND)

# Input of data from user
total_tickets_amount = int(input("\nType the quantity of tickets you would like to buy: "))
adult_quantity = int(input("Type quantity of adults tickets: "))
children_quantity = int(input("Type quantity of children tickets: "))
concessions_quantity = int(input("Type quantity of concessions tickets: "))

# calculate chaperone places
chaperone = int((children_quantity / 10))
ticket_cost = ((adult * adult_quantity) + (child * children_quantity) + (concessions_quantity * concessions))

if chaperone >= 1:
    free_adults = int(chaperone)
    print(CGREEN + "\nFree adults: {}".format(free_adults) + CEND)
else:
    print(CRED + "\nNo free adults tickets available. " + CEND)

discount_chaperone = float(chaperone * adult)
bill_cost = (ticket_cost - discount_chaperone)

# discount calculation
if bill_cost > 100:
    print(CGREEN + "Discount of 10% applied. " + CEND)
    total_bill = (bill_cost - (bill_cost * 0.1))
else:
    print(CRED + "No discount applied." + CEND)

# ticket delivery
tickets_delivery = str(input("\nWould like the tickets to be delivered (Y/N)? "))
if tickets_delivery == "Y" or tickets_delivery == "y":
    additional_cost = float(2.34)
    total_cost = additional_cost + total_bill
    print("Your tickets will be delivered.")
    print("Additional cost: £{:.2f}".format(additional_cost))
    print("Total cost: £{:.2f}".format(total_cost))
else:
    print("You can collect in person. No additional costs. ")
    total_cost = total_bill
    print("Total cost: £{:.2f}".format(total_cost))

# end of algorithm

# I could improve the algorithm by validating all the data / validation on the 1 adult requirement at least ...
