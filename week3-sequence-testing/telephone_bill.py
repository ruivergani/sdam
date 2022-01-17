# Program that calculate telephone bill
print("\nWelcome to exercise 1 (week - 3) of SDAM")

# variables
minutes = int(input("\nType the quantity of minutes used: "))

# calculations
call_charge = float((minutes * 0.15))
vat = float((call_charge * 0.20))
total_bill = float((call_charge + vat))

# output data2
print("\nNumber of minutes used: {}" .format(minutes))
print("Basic call charge: £ {:.2f}" .format(call_charge))
print("VAT due: £ {:.2f}" .format(vat))
print("Total bill: £ {:.2f}" .format(total_bill))