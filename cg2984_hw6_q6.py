#Clara Gilligan
#Homework 6
#CS 1114
#10/30/18

def count_doubled(s):
    count = 0
    for i in range(len(s)):
        if s[i] == s[i-1]:
            count+=1
    return count
def main():
    string = input("Enter a string: ")
    print(count_doubled(string))
main()
            
        
