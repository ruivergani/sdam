import random
import math


def register():
    db = open("database.txt", "r")
    username = str(input("Create username: "))
    password = str(input("Create password: "))
    password_confirm = str(input("Confirm password: "))
    d = []  # empty list to store password
    f = []  # empty list to store username
    for i in db:
        a, b = i.split(", ")  # split the text file data
        b = b.strip()  # remove any char in the password
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    print(data)

    if password != password_confirm:
        print("Passwords do not match, restart...")
    else:
        if len(password) <= 6:
            print("Password too short.")
            register()
        elif username in d:
            print("Username exists.")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username + ", " + password + "\n")
            print("Success!")


def access():
    db = open("database.txt", "r")
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    if not len(username or password) < 1:
        d = []  # empty list to store password
        f = []  # empty list to store username
        for i in db:
            a, b = i.split(", ")  # split the text file data
            b = b.strip()  # remove any char in the password
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login success.")
                        print("Hi, ", username, " Welcome.")
                    else:
                        print("Incorrect details.")
                except:
                    print("Incorrect password of username.")
            else:
                print("Username or password does not exist.")
        except:
            print("Username or password does not exist.")
    else:
        print("Please enter a value. ")

def home(option=None):
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option.")


# Start of the program
home()  # calling the function
