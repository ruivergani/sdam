# rainfall algorithm

# use dictionary

months = {}
counter = int(12)

for i in range(counter):
    key = str(input("\nEnter the month:"))
    value = int(input("Enter the rain:"))
    months.update({key: value})

# user typed
for months, rain in months.items():
    print(months, "->", rain)

