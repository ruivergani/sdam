# password exercise

password_stored = str("Rocket")
user_password = ""
while password_stored != user_password:
    user_password = str(input("\nType a password: "))
    if password_stored == user_password:
        print("Welcome to the system!")
        break
    else:
        print("Try again")
