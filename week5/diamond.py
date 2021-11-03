# diamond exercise

num = int(input("Type the length: "))

while (num > 2) and (num < 40):
    for i in range(1, num+1):
        i = i - (num//2 + 1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (num - i*2) + " "*i)
    num = int(input("Type the length: "))
else:
    print("Wrong input (out of range), try again.")
    exit
