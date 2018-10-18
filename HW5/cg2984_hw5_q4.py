#Clara Gilligan
#Homework 5
#CS 1114
#10/17/18
s = input("Enter a string: ")
newS = ""
for i in range(len(s)):
    s[i]
    if i == 0:
        newS+=s[i].upper()
    elif s[i-1] == " ":
        newS+=s[i].upper()
    elif s[i-1] == "!" or s[i-1] == "." or s[i-1] == "," or s[i-1] == ":"or s[i-1] == ";" or s[i-1] == "(" or s[i-1] == ")" or s[i-1] == "?":
        newS+=s[i].upper()
    else:
        newS+=s[i]
print(newS)
        
    
