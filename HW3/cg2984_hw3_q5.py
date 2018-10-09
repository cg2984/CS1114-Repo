#Clara Gilligan
#CS 1114
#10/2/18
#Homework 3

import math
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
discriminant = (b**2)-(4*a*c)



if a == 0:
    posFormula = ((-1*b)+math.sqrt(discriminant))/2*a
    print("There is one solution: " + str(posFormula))
elif a > 0:
    if discriminant < 0:
        print("Solution is Imaginary.")
    elif discriminant > 0:
        negFormula = ((-1*b)-math.sqrt(discriminant))/2*a
        posFormula = ((-1*b)+math.sqrt(discriminant))/2*a
        print("There are two solutions: " + str(negFormula) + " " + str(posFormula))
    elif discriminant == 0:
        posFormula = ((-1*b)+math.sqrt(discriminant))/2*a
        print("There is one solution: " + str(posFormula))
else:
    print("Something is wrong.")
    
