# ARAN (Student) code in order to analyse and share knowledge

card_hide = [["*","*","*","*"],["*","*","*","*"],["*","*","*","*"],["*","*","*","*"]]
card_show = [["J","Q","K","A"],["A","J","Q","K"],["K","A","J","Q"],["Q","K","A","J"]]


#for x in range (0,4):
   # for y in range(0,4):
  #      print(card_show[x][y], end= "\t")
 #       if(x == 4):
#            print("\n")

for r in card_hide:
    for c in r:
        print(c,end=" ")
    print()

##row left to right
##colums up and down
## [0][1] is Q - So [a][b] a columns - {so y} ; b row - {so x}
print(card_show[0][1])


while(card_show != card_hide):
    print("Choice 1: ")
    c1_c = int(input("Enter the column :"))
    c1_r = int(input("Enter the row :"))

    hold_pos1 = card_show[c1_c][c1_r]

    print("Choice 2: ")
    c2_c = int(input("Enter the column :"))
    c2_r = int(input("Enter the row :"))

    hold_pos2 = card_show[c2_c][c2_r]

    if (card_show[c1_c][c1_r] == card_show[c2_c][c2_r]):
        print("Duplicate")
        card_hide[c1_c][c1_r] = card_show[c2_c][c2_r]
        card_hide[c2_c][c2_r] = card_show[c1_c][c1_r]

        if (hold_pos1 == "J"):
            print("Two Jacks")
            #card_hide[c1_c][c1_r] = card_show[c1_c][c1_r]
        elif (hold_pos1 == "K"):
            print("Two Kings")
            #card_hide[c1_c][c1_r] = card_show[c1_c][c1_r]
        elif (hold_pos1 == "Q"):
            print("Two Queens")
            #card_hide[c1_c][c1_r] = card_show[c1_c][c1_r]
        elif (hold_pos1 == "A"):
            print("Two Aces")
            #card_hide[c1_c][c1_r] = card_show[c1_c][c1_r]

    for r in card_hide:
            for c in r:
                print(c, end=" ")
            print()
