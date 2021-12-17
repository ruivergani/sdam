# odd or even exercise

number = int(input("\nType a number: "))

# calculations and output
temp = number % 2

if number == 0:  # if statement condition
    print("Result: Neutral number")
elif temp == 0:
    result = bool(True)
    print(result)
else:
    result = bool(False)
    print(result)



