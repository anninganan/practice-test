username=["alex","phonix","rio","sanhand","xiamrun","steve"]
login=input("Enter your username: ").lower().strip()
while login not in username:
  print("Invalid username")
  login=input("Enter your username: ").lower().strip()
print("login successful")
print("quiz start")
score=0
Dictionary = {"Gerry Austin steals a wallet and uses the cash to rent a Mini. Which is the colour of MIni?     A) white  B) yellow C) black D) red":"B",
              "Gerry and John pick up___,who is heading to Wanganui A Sue B Shirl  C Mulvaney  D YOU":"B",
              "Who helps the trios in wellington?   A Sue B Shirl  C Mulvaney D YOU":"C",
              "Who is the director of this movie(Goodbye Pork Pie)?   A Geoff Murphy  B John coker  C Tony Barry  D YOU":"A",
              "This movie release at ___year (Goodbye Pork Pie)   A 1985  B 1991  C 2024  D 1981":"D"}
for x in Dictionary:
    print(x)
    answer=input("Your answer is  :")
    validate_answers=['A','B','C','D']
    while answer  not in validate_answers:
        print("invalid answer answer should in A B C D")
        answer=input("your answer is :")
        print(validate_answers)
    else:
        print("your answer is"+ answer)
        if answer==Dictionary[x]:
            print("correct")
            score+=1
            print("your score is: ",score)
        else:
            print("Incorrect,the answer is",Dictionary[x])
if score==3 or score==4 :
    print("well done!but still need learn about it.")
if score==1 or score==2:
    print("you need watch more about it")
if score== 5 :
    print("awsome,you pass this quiz")
        
        
