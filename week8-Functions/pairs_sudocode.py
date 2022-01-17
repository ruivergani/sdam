# display an initial grid

card = (('J', 'Q', 'K', 'J'),
        ('A', 'K', 'Q', 'J'),
        ('Q', 'A', 'K', 'A'))

print('')
j = 0
for item in range(len(card)):
    print(item, end=" ", sep=" ")
    for j in range(len(card[item])):
        print(card[item][j], end=" ")
    print()

