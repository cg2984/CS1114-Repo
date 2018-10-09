#Clara Gilligan
#10/2/18
#CS 1114
#Homework 3

import random


randNum = random.randint(0,2)
playerChoice = input("Rock, Paper, or Scissors: ")
compChoice = "Rock"

if randNum == 0:
    compChoice = "Rock"
elif randNum == 1:
    compChoice = "Paper"
elif randNum == 2:
    compChoice = "Scissors"
else:
    print("Computer has not chosen")


print("Player has chosen: " + playerChoice)
print("Computer has chosen: " + compChoice)

if playerChoice == "Rock" and compChoice == "Rock":
    print("Tie!")
elif playerChoice == "Rock" and compChoice == "Paper":
    print("Computer Wins!")
elif playerChoice == "Rock" and compChoice == "Scissors":
    print("Player Wins!")
elif playerChoice == "Paper" and compChoice == "Paper":
    print("Tie!")
elif playerChoice == "Paper" and compChoice == "Rock":
    print("Player Wins!")
elif playerChoice == "Paper" and compChoice == "Scissors":
    print("Computer Wins!")
elif playerChoice == "Scissors" and compChoice == "Scissors":
    print("Tie!")
elif playerChoice == "Scissors" and compChoice == "Paper":
    print("Player Wins!")
elif playerChoice == "Scissors" and compChoice == "Rock":
    print("Computer Wins!")
else:
    print("The options are wrong")
