haystack = ["tree", "flower", "grass"]
needle = "something else"

for item in haystack:
    if item == needle:
        print("The item was found.")
        break
else:
    print("The item wasn't found.")

