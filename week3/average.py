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

# week 3
# Sequence: step by step
# Iteration: repetitive statement = loop (do, while, for)
# Selection = choose (if/elif/else)
# syntax error (machine error or code) | logical error (does not give message, executes, but result is wrong) | runtime error (division 0)
# Test plan: input | reason | expected | actual
# Debug is the process of removing errors