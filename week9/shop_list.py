# shop list exercise

cancel = False
class_list = {}

while (True):
    product = input("\nProduct: ")
    price = float(input("Price: £"))
    class_list.update({product: price})
    cont = input("Want to add another? (Y/N):")
    if cont == "N" or cont == "n":
        break

print("\nDictionary: ", class_list)

# sorting and display dictionary
sorted_values = sorted(class_list.values())  # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in class_list.keys():
        if class_list[k] == i:
            sorted_dict[k] = class_list[k]
            break
print("Sorted Dictionary: ", sorted_dict)