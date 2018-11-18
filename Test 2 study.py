'''
#Problem 1: short+long+short strings
def combo_string(a, b):
    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b
def main():
    stringA = input("Enter string A: ")
    stringB = input("Enter string B: ")
    print(combo_string(stringA, stringB))
main()
'''
#Problem 2: Find xyz in a string
def xyz_there(string):
    isXYZ = False
    string = string.lower()
    for i in range (len(string)):
        if string[i:i+3] == "xyz":
            isXYZ = True
            print(string[i:i+3])
        elif string[i:i+4] == ".xyz":
            isXYZ = False
            print(string[i:i+4])
    if isXYZ == True:
        return "XYZ is there"
    else:
        return "XYZ is not there"
def main():
    string = input("Enter a string: ")
    print(xyz_there(string))
main()
#P
def LongestWord(sen): 
    longestLen = 0
    longestWord = ''
    wordList = sen.split()
    for word in wordList: 
        tempWord = ''
        for letter in word: 
            if letter.isalnum():
                tempWord+=letter
        if len(tempWord)> longestLen:
            longestLen = len(tempWord)
            longestWord = tempWord
    return longestWord   

print LongestWord(raw_input()) 
