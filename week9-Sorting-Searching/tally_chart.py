# tally chart algorithm

def insertion_sort_ascending(data):   # declare function
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


counter = 0
results = []
c_rui = 0
c_neto = 0
c_gabor = 0
c_jordan = 0
while counter != 1:
    # DISPLAY CANDIDATES
    print("\nList of candidates: ")
    print("2: Rui")
    print("3: Neto")
    print("4: Gabor")
    print("5: Jordan")
    print("1 to exit")
    user_vote = int(input("Type the code for your vote: "))
    if user_vote == 1:
        counter = 1
        exit
    elif user_vote == 2:
        c_rui += 1
        print("\n** Vote computed for Rui. **")
        print("Rui: ", c_rui, " votes.")
    elif user_vote == 3:
        c_neto += 1
        print("\n** Vote computed for Neto. **")
        print("Neto: ", c_neto, " votes.")
    elif user_vote == 4:
        c_gabor += 1
        print("\n** Vote computed for Gabor. **")
        print("Gabor: ", c_gabor, " votes.")
    elif user_vote == 5:
        c_jordan += 1
        print("\n** Vote computed for Jordan. **")
        print("Jordan: ", c_jordan, " votes.")
    else:
        print("You haven't selected a candidate, try again...")
        exit
else:
    exit

results.append(c_rui)
results.append(c_jordan)
results.append(c_neto)
results.append(c_gabor)

insertion_sort_ascending(results)
print("\nSorted array is:")
print(results)

list_of_numbers = results
max_value = list_of_numbers[0]

for element in list_of_numbers:
    if element > max_value:
        max_value = element
print("The candidate winner received: ", max_value, "votes")

if max_value == c_rui:
    print("Winner is Rui.!")
elif max_value == c_jordan:
    print("Winner is Jordan!")
elif max_value == c_neto:
    print("Winner is Neto!")
elif max_value == c_gabor:
    print("Winner is Gabor!")








