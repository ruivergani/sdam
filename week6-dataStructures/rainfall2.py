# rainfall oficial

print("\n")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rain = []
i = 0

# enter in the rain list the values
for i in range(len(months)):
    x = int(input("Enter the rain for " + months[i] + ": "))
    rain.append(x)

print("\n")

# print all the values from list
for i in range(len(months)):
    counter = rain[i]
    print(months[i] + ": " + (counter*" x "))

