# Clara Gilligan
# CS - UY 1114
# 13 Sept. 2018
# Homework 1

quarters = int(input("Number of quarters ")) * 25
dimes = int(input("Number of dimes ")) * 10 
nickels = int(input("Number of nickels ")) * 5
pennies = int(input("Number of pennies "))

total_val = quarters + dimes + nickels + pennies
dollar_val = total_val // 100
cent_val = total_val - (dollar_val * 100)

print("The total is " + str(dollar_val) + " dollar(s) and " + str(cent_val) + " cents.")





