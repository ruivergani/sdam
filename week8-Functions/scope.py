# local variables and global variables

def local_test():
    spam = "Spam in function"

def global_test():
    global spam
    spam = "Global spam"

spam = "Spam in module"

local_test() # local variable
print(spam)

global_test() # global variable
print(spam)