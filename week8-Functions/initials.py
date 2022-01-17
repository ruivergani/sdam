# initials exercise

def initials():
    name = input("\nEnter your first name followed by surname: ")
    string_split = name.split(" ")

    print("List is: {}" .format(string_split))
    print("Initials: {} {} " .format(string_split[0][0], string_split[1][:1]))

initials()
