#Clara Gilligan
#CS 1114
#Homework 4
#10-7-18

binary = input("Enter a binary number: ")
binaryLength = len(binary)
count = 1
total = 0
binaryPos = binaryLength
for i in range(binaryLength):
    if binary[i] == '1':
        total += 2**(binaryLength-count)
        print(binary[i],total)
    else:
        total +=0
        print(binary[i],total)
    count+=1
print(total)




