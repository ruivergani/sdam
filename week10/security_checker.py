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
                if (len(password) <=8):
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
            # save data to file (nested dictionary not used)
            passwords = {"username": username, "password": password}
            json_string = json.dumps(passwords, indent=2)
            # write into the JSON file
            with open('password.json', 'a') as file_object:
                json.dump(passwords, file_object)

        elif option == 2:
            print("Option 2")
            # enter username and password anc check against json file
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
