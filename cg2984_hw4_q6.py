#Clara Gilligan
#CS 1114
#Homework 4
#10-7-18

import random
randNum = random.randint(1,100)
guessNum = int(input("Enter a number: ")
while randNum != guessNum: 
  if guessNum > randNum: 
    print("The number was too high, go lower")
    guessNum = int(input("Enter a number: ")
  elif guessNum < randNum:
    print("The number was too low, go higher")
    guessNum = int(input("Enter a number: ")
  elif not guessNum.isdigit():
    print("Please enter a number")
    guessNum = int(input("Enter a number: ")
print("Congrats! You guessed the number!")
