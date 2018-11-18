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
#Problem 3
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
#Problem 4
def AlphabetSoup(string): 
    alphaList = []
    alphaSorted = []
    smallestChara = 124
    smallestPlace = 0
    for letter in string:
        alphaList.append(letter)
    for i in range(alphaList): 
        if ord(alphaList[i]) < smallestChara:
            smallestList = i
            smallestChara = ord(alphaList[i])
    return alphaSorted
    
# keep this function call here  
print AlphabetSoup(raw_input()) 

#Problem 5
def LetterCapitalize(string):
    stringList = string.split()
    newString = []
    for word in stringList: 
        newWord = word[0].upper() + word[1:]
        newString.append(newWord)
    newString = " ".join(newString)
    return newString
    
# keep this function call here  
print LetterCapitalize(raw_input())  
