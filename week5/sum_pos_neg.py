# sum_pos_neg
n = 0
positive = 0
negative = 0
while n < 10:
    number = int(input("\nType either a positive or negative number: "))
    # calculations
    if number > 0:
        positive = positive + number
        n += 1
    else:
        negative = ((- number) + negative)
        n += 1

# output
print("\nSum of positive: {} " .format(positive))
print("Sum of negative: -{} " .format(negative))

