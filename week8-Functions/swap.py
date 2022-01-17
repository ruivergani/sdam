# swap algorithm

def swap(num1, num2):
    temp = num1
    mylist[0] = num2
    mylist[1] = temp

def print_int_list(num1, num2):
    swap(num1, num2)
    print("List: ", mylist)


num1 = int(input("\nType the first number: "))
num2 = int(input("Type the second number: "))

mylist = [num1, num2]

swap(num1, num2)
print_int_list(num1, num2)
