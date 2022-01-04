# login system using class
import getpass


class User:
    def __init__(self, name, email, password, login):  # automatic method
        self.name = name
        self.email = email
        self.password = password
        self.login = login

    def Login(self):
        email = str(input("Enter your e-mail: "))
        password = getpass.getpass()

        if self.email == email and self.password == password:
            print("Login success \n", self.name, "\n", self.email)
        else:
            print("Login failed. Try again...")


user1 = User('Rui Vergani Neto', 'ruiverganineto@gmail.com', 'testing12345', False)  # calling the class with the attributes and methods
user2 = User('Gabor Oravecz', 'gabor@gmail.com', 'testing12345', False)

user1.Login()  # executing another method
