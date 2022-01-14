# create list
my_list = ['Jessa', 10, 20, 'Kelly', 50, 10.5]
# print entire list
print(my_list)  # ['Jessa', 10, 20, 'Kelly', 50, 10.5]

# Accessing 1st element of a list
print(my_list[0])  # 'Jessa'

# Accessing  last element of a
print(my_list[-1])  # 10.5

# access chunks of list data
print(my_list[1:3])  # [10, 20]

# Modifying first element of a list
my_list[0] = 'Emma'
print(my_list[0])  # 'Emma'

# add one more elements to list
my_list.append(100)
print(my_list)  # ['Emma', 10, 20, 'Kelly', 50, 10.5, 100]