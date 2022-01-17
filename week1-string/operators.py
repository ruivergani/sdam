x = 10
y = 5
z = 2

# > Greater than
print(x > y)  # True
print(x > y > z)  # True

# < Less than
print(x < y)  # False
print(y < x)  # True

# Equal to
print(x == y)  # False
print(x == 10)  # True

# != Not Equal to
print(x != y)  # True
print(10 != x)  # False

# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True

# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True

# is operator
x = 10
y = 11
z = 10
print(x is y) # it compare memory address of x and y
print(x is z) # it compare memory address of x and z