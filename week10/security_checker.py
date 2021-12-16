# menu password system
import json
import math
import re

print()
option = 0
counter = 0

while option != 3:
    counter += 1
    # menu display
    print("\n1. New user")
    print("2. Existing user")
    print("3. Exit Program")

    try:
        option = int(input("\nType your choice: "))
        if not (0 < option < 3):
            raise Exception
        if option == 1:
            username = str(input("\nUsername: "))
            count = 1
            # validation for password
            while True:
                password = str(input("Password: "))
                is_valid = False
                if len(password) <= 8:
                    print("\nNot valid! Must be at least 8 characters long.")
                    print()
                    continue
                elif re.search("[\s]", password):
                    print("\nIt should not contain spaces.")
                    print()
                    continue
                elif password[0].isdigit():
                    print("\nShould not begin with a number.")
                    print()
                    continue
                else:
                    is_valid = True
                    break
            # end of while
            while True:
                password2 = str(input("Confirm Password: "))
                is_valid2 = False
                if password != password2:
                    print("\nPasswords are different.")
                    continue
                else:
                    print("\nPassword confirmed.")
                    is_valid2 = True
                    break
            if is_valid:
                print("** Password is valid **")

            # function to append data into file
            def write_json(new_data, filename='data.json'):
                with open(filename, 'r+') as file:
                    file_data = json.load(file)
                    file_data["user_details"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
            # Python object to be appended
            data = {"username": username, "password": password}
            write_json(data)

        elif option == 2:
            # load data from the file
            f = open('data.json')
            data = json.load(f)
            while True:
                turns = 0
                if turns > 3:
                    print("You are locked out.")
                    exit()
                else:
                    username_user = input("\nEnter username: ")
                    for i in data['user_details']:
                        if username_user == i['username']:
                            # validation for password
                            while True:
                                password_user = str(input("Password: "))
                                is_valid = False
                                if len(password_user) <= 8:
                                    print("\nNot valid! Must be at least 8 characters long.")
                                    print()
                                    continue
                                elif re.search("[\s]", password_user):
                                    print("\nIt should not contain spaces.")
                                    print()
                                    continue
                                elif password_user[0].isdigit():
                                    print("\nShould not begin with a number.")
                                    print()
                                    continue
                                else:
                                    if password_user == i['password'] and username_user == i['username']:
                                        print("Welcome to the system.")
                                        exit()
                                    else:
                                        print("Try again...")
                                        turns += 1
                                        break
                            # end of while
                            break
                            False
                        else:
                            continue

        else:
            print("Wrong Option")

    except ValueError:
        print("Requires an integer type.")

    except Exception:
        if option == 3:
            print("Exiting program...")
        elif not (option == 1 or option == 2):
            print("Requires an integer between 1 and 2.")
else:
    exit()
