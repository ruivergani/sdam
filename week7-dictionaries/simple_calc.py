# simple calc exercise

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
operator = input("Type the operator (+, -, / or *): ")
if operator == "+":
    result = (num1 + num2)
    print("\nYour sum is {} {} {} and the answer is {} " .format(num1, operator, num2, result))
elif operator == "-":
    result = (num1 - num2)
    print("\nYour subtraction is {} {} {} and the answer is {} " .format(num1, operator, num2, result))
elif operator == "/":
    result = (num1 / num2)
    print("\nYour division is {} {} {} and the answer is {} " .format(num1, operator, num2, result))
elif operator == "*":
    result = (num1 * num2)
    print("\nYour multiplication is {} {} {} and the answer is {} " .format(num1, operator, num2, result))
else:
    print("\nWrong input operator.")