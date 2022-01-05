# average pi number

count = int(input("How many numbers? "))
total_sum = 0

for n in range(count):
    numbers = float(input("Enter any number: "))
    total_sum += numbers

avg = total_sum / count
print("Average is: {:.2f}" .format(avg))
