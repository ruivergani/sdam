# example of using class

class Person:
    def __init__(self, name, age):
        self.name = name # self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
        self.age = age

    def myfunc(self):
        print("Hello my name is ", self.name)


p1 = Person("Rui", 20)
p1.myfunc()