# alphabetical algorithm

thislist = []
counter = 1
while counter < 6:
    text = str(input("\nPlease enter " + str(counter) + " list: "))
    thislist.append(text)  # add number to the list
    counter += 1

thislist.sort()
print("\nNormal: ", thislist)
thislist.reverse()
print("\nReversed: ", thislist)