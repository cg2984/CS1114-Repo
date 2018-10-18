#Clara Gilligan
#Homework 5
#CS 1114
#10/17/18

password = input("Enter a string: ")
rePassword = ""
upperCounter = 0
numCounter = 0
isNum = False
isUpper = False
isLower = False
isSpec = False 
for i in range(len(password)):
    password[i]
    rePassword+=password[i]
    if ord(password[i]) >= 65 and ord(password[i]) <= 90:
        upperCounter+=1
        if counter >= 2:
            isUpper = True
    elif ord(password[i]) >= 97 and ord(password[i]) <= 122:
        isLower = True
    elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
        numCounter+=1
        if numCounter >= 2:
            isNum = True
    elif password[i] == "!" or password[i] == "@" or password[i] == "#" or password[i] == "$":
        isSpec = True
    
