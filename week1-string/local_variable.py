def test1():  # defining 1st function
    price = 900  # local variable
    print("Value of price in test1 function :", price)

def test2():  # defining 2nd function
    # NameError: name 'price' is not defined
    print("Value price in test2 function:", price)

# call functions
test1()
test2()