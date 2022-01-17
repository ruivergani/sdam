# grid exercise

row = int(input("\nEnter the number of rows: "))
column = int(input("Enter the number of columns: "))

# calculations to generate matrix

grid = ""
for i in range(row):
    grid += "\n"
    for j in range(column):
        grid += (" * ")

print(grid)
