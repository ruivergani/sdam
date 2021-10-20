# Calculate the average of 4 numbers input

# variables
n = 0  # counter max num avg
sum = 0

# calculations
while n < 4:
    number = int(input("\nEnter the {} number (integer): " .format(n)))
    sum += number  # store all numbers typed by user
    n += 1  # put counter up (increment)

average = float(sum / 4)

# output
print("\nTotal Sum: ", sum)
print("Average is: {:.2f}" .format(average))