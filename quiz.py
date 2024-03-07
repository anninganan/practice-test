score=0
Dictionary = {"Gerry Austin steals a wallet and uses the cash to rent a Mini. Which is the colour of MIni?     A white  B yellow C black D red":"B",
              "Gerry and John pick up___,who is heading to Wanganui A Sue B Shirl  C Mulvaney  D YOU":"B",
              "Who helps the trios in wellington?   A Sue B Shirl  C Mulvaney D YOU":"C",
              "Who is the director of this movie(Goodbye Pork Pie)?   A Geoff Murphy  B John coker  C Tony Barry  D YOU":"A",
              "This movie release at ___year (Goodbye Pork Pie)   A 1985  B 1991  C 2024  D 1981":"D"}
for x in Dictionary:
    print(x)
    answer=input("Your answer is  :")
    if answer==Dictionary[x]:
        print("correct")
        score+=1
    elif answer!=["A","B","C","D"]:
        print("invaild NSWER, answer should in ABCD")
        
    else:
        print("uncerrect")
        
