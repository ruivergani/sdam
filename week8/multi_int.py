# multi int exercise

def initials():
    name = str(input("\nEnter your full name: "))
    string_split = name.split(" ")
    print("List: ", [i.strip() for i in string_split])
    new_list = [elem for elem in string_split if elem.strip()] # remove spaces in list
    print("List (no spaces): ", new_list)

    i = 1
    for i in range(len(new_list)):
        s = new_list[i][:1]
        print(s)
        i += 1


initials()
