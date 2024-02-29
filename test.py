credentials={"David":"123456","Alex":"password","Maria":"qwerty","Anna":"dragon","Marco":"baseball","Antonio":"abc123"}
print(credentials)

user=input("enter your user name")

while user in credentials:
    print("username registered")
    password = input("please enter your password : ")
    if password==credentials[user]:
        print("log in")
    else :
        print("password is wrong. try again please.")
        password = input("please enter your password : ")
else:
    print("username not registered")   

