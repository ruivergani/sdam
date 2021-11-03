# average pos_neg

n = 0
counter_pos = 0
counter_neg = 0
positive = 0
negative = 0

while n < 10:
    number = int(input("\nType either a positive or negative number: "))
    # calculations
    if number > 0:
        positive = positive + number # sum of all positives
        counter_pos = counter_pos + 1
    else:
        negative = ((- number) + negative) # sum of all negatives
        counter_neg = counter_neg + 1
    n += 1

# output
neg = - negative

if positive == 0:
    print("\nNo positive numbers entered. Try again.")
    print("Sum of positive: {} ".format(positive))
    print("Average: 0")
else:
    average_pos = float((positive / counter_pos))
    print("\nSum of positive: {} ".format(positive))
    print("Average of positive: {} ".format(average_pos))

if negative == 0:
    print("\nNo negative numbers entered. Try again.")
    print("Sum of negative: {} ".format(neg))
    print("Average: 0")
else:
    average_neg = float(-(neg / counter_neg))
    print("\nSum of negative: {} " .format(neg))
    print("Average of negative: {} " .format(average_neg))

