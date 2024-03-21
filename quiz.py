#creat a list about username,use input function to let user input their name to login
username=["alex","phonix","rio","sanhand","xiamrun","steve","a"]
login=input("Enter your username: ").lower().strip()
#use while loop to check the username is valid or invalid.
while login not in username:
  print("Invalid username")
  login=input("Enter your username: ").lower().strip()
print("login successful")
print("quiz start")
#creat a function abouut quiz
def quiz():
  #login successful, quiz begin and record the score
  score=0
#creat a dictionary involve five question, use for loop to print question and user answer question in order.
  Dictionary = {"Gerry Austin steals a wallet and uses the cash to rent a Mini. Which is the colour of MIni?     A) white  B": "yellow",
  "Gerry and John pick up___,who is heading to Wanganui A Sue B Shirl  C Mulvaney  D YOU": "B",
  "Who helps the trios in wellington?   A Sue B Shirl  C Mulvaney D YOU": "C",
  "Who is the director of this movie(Goodbye Pork Pie)?   A Geoff Murphy  B John coker  C Tony Barry  D YOU": "A",
  "This movie release at ___year (Goodbye Pork Pie)   A 1985  B 1991  C 2024  D 1981": "D"}
  for x in Dictionary:
      print(x)
      answer=input("Your answer is  :").upper().strip()
    #use while loop to check the answer, which the user input, is valid or invalid. If the answer is invalid, user will
    #fall in a loop untill they input a valid answer.
      validate_answers=['A','B','C','D']
      while answer  not in validate_answers:
          print("invalid answer, answer should in A B C D")
          answer=input("your answer is :").upper().strip()
          print(validate_answers)
    #The answer is valid, then begin to check the answer. If right, score +1.. If wrong, print the right answer.
      else:
          print("your answer is"+ answer)
          if answer==Dictionary[x]:
              print("correct")
              score+=1
              print("your score is: ",score)
          else:
              print("Incorrect,the answer is",Dictionary[x])

#According to the score print different result to console
  if score==3 or score==4 :
      print("well done!but still need learn about it.")
  if score==1 or score==2:
      print("you need watch more about it")
  if score== 5 :
      print("awsome,you pass this quiz")
quiz()
  #if user want play it more, user can input y or n, if y, the quiz will start again, if n, the code will end.
play=input("Do you want to play again(yes/no)?")
  #while loop can let user play it again and again if they want.
while play =="yes":
  quiz()
  play=input("Do you want to play (yes/no)?")
