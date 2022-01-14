# week 1
# P E M D A S = () ** * / + -
# // floor division (int value)
# % rest of division
# / = type special character | '' or "" or """ """ as long is consistent
# print(sep=''  separate objects, end='\n' default new line, file=sys.stdout sent to default stdout, flush=False force buffer)
# snake case = name_variable
# str() int() float() bool()

# week 2
# .capitalize() = first letter capital
# .title() =
# .format() = format to string
# .join() = join iterables
# .lower() = lowercase
# .rjust() = right justified
# .ljust() = left justified
# .split() = split string
# .strip() = remove whitespace
# input holds String value | remember python only prints String value (str(round,2) for example
# An escape character is a backslash \ followed by the character you want to insert.

# week 3
# Sequence: step by step
# Iteration: repetitive statement = loop (do, while, for)
# Selection = choose (if/elif/else)
# syntax error (machine error or code) | logical error (does not give message, executes, but result is wrong) | runtime error (division 0)
# Test plan: input | reason | expected | actual
# Debug is the process of removing errors

# week 4
# Selection (IF STATEMENT) = if elif else
# not(x>y) result is False (x = 4 and y = 3) (will always be the opposite)
# Logical and Operational Operators

# Lists: mylist=["apple", "banana"] (different data type, multiple values, allow duplicate, changeable)
# Tuples: mytuple=("apple", "banana") (store in a single variable, unchangeable)
# Sets: thisset={"apple", "banana"} (unordered, unchangeable, no index, no duplicate items)
# Dictionary: data in key:value pairs, thisdic={"brand":"ford"} | mutable | using keys index | no duplicate | ordered

# week 5
# deterministic x non-deterministic
# range(1,6) - range(5, 51, 5) = start, stop, step | range(10, 0, -1) = negative progression [10,9,8,7,6,5,4,3,2,1]
# while i < 6:
#   print(i)
#   i += 1
# for x in fruits:
#   print(x)

# week 6
# List:
# months[5]="Jun"
# mylist += ["Saturday"]
# mylist.append("Saturday")
# mylist.extend(["Saturday"],["Sunday"])

# Tuples:
# months = ("January", "February", "March")
# Slicing: [fromposition : to position : step]
# mylist.append()
# mylist.insert()
# mylist.extend()
# mylist.pop()
# mylist.clear()
# mylist.index()
# mylist.count()
# mylist.sort()
# mylist.reverse()

# Dictionaries
# months = {"Jan":31, "Feb":28}
# months['Feb']=28
# .keys() | .values() | .items()
# thisdic.update({"March": 30})
# thisdic.pop("model") or .popitem() or del thisdic or del thisdic["model"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[6:2:-2])
['mango', 'kiwi']

# Negative indexing means starting from the end of the list.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1,


# Functions:
# def name(parameter):
# def formatrow(header=False) = default value parameter
# id() : give id in memory
# len(): length of the data sequence or collection
# reversed(): print reversed items
# sorted(): print sorted items
# filter(): filter elements
# map(): (function, iterable) - will go through every item on the iterable
# open(): open file object

fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
fullname("    leonard", "EULER")
print(fullname)

# week 10
# Exception Handling:
# ZeroDivisionError: when dividend is zero
# IndexError: out of range sequence num
# KeyError: dictionary key not found
# FileNotFoundError: file not found
# TypeError: wrong type operation = '1' + 1
# ValueError: correct type wrong value = int('six')
# if not(0 < guess < 6): raise ValueError
# try: code cause an exception
# except Exception: runs when exception occurs
# else: if no exception occurs
# finally: runs after try block or except block

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



