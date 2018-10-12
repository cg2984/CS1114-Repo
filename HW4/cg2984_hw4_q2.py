#Clara Gilligan
#CS 1114 
#Homework 4
#10-7-18

n = int(input("Enter a positive integer: "))
initial = 3
multiples = 0
factor = 0
i = 0
while i < n:
  factor += 1
  multiples = initial*factor
  print(multiples)
  i+=1
print("Done")
  
