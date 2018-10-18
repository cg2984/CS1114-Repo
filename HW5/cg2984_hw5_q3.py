#Clara Gilligan
#Homework 5
#CS 1114
#10/17/18

s = input("Enter a string: ")
isPunc = False
for i in range(len(s)):
    s[i]
    if s[i] == "!" or s[i] == "." or s[i] == "," or s[i] == ":"or s[i] == ";" or s[i] == "(" or s[i] == ")" or s[i] == "?":
        isPunc = True
    else:
        isPunc = False
if isPunc == True:
    print("There is puncuation in this string.")
elif isPunc == False:
    print("There is no puncuation in this string.")
