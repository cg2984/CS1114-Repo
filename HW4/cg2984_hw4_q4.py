#Clara Gilligan
#CS 1114
#Homework 4
#10-7-18

import turtle
sides = int(input("How many sides? "))
length = int(input("How long should the sides be? "))

for i in range(0,sides):
  turtle.forward(length)
  turtle.right(360/sides)
 

