# magpie exercise
number = 0
n = 0
while n == 0:
    number = int(input("\nType a number in 1-7 range: "))
    if (number <= 7) and (number >= 1):
        print("Correct input number!")
        n = 1
        # second row of calculations
        if number == 1:
            print("\nOne for sorrow! ")
        elif number == 2:
            print("\nTwo for joy")
        elif number == 3:
            print("\nThree for a girl")
        elif number == 4:
            print("\nFour for a boy")
        elif number == 5:
            print("\nFive for silver.")
        elif number == 6:
            print("\nSix for gold. ")
        elif number == 7:
            print("\nSeven for a secret never to be told")
        break
    else:
        print("Incorrect input format.")
        n = 0