haystack = ["tree", "flower", "grass"]
needle = "something else"

for item in haystack:
    if item == needle:
        print("The item was found.")
        break
else:
    print("The item wasn't found.")

# week 11 (File Handling)
# open(
#     <file>,
#     mode='r',
#     buffering=-1,
#     encoding=None,
#     errors=None,
#     newline=None,
#     closefd=True,
#     opener=None
# )
# R: read  A: append W: write X: create
# f = open("demofile.txt", "r")

# for loop example
basket = ['juice', 'cereal', 'lemons']
for item in basket:
    print(item)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


