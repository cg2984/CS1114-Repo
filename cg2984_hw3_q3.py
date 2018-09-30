#Clara Gilligan
#9/29/18
#Homework 3
#CS 1114

15rate = 0.15
25rate = 0.25
40rate = 0.40

callDay = input("Please enter the day the call started: ")
callTime = int(input("Please enter the time of the call (hhmm): "))
callDuration = int(input("Please enter the duration of the call in minutes: "))

if callDay = Sat or Sun:
  callCost = callDuration * 15rate
elif callDay = Mon or Tue or Wed or Thur or Fri: 
  if callTime > 0800 or callTime 1800:
    callCost = callDuration * 40rate
  elif callTime < 0800 or callTime > 1800:
    callCost = callDuration * 15rate
else: 
  print("Nothing has been written.")
  
cents = callCost % 100 
dollars = callCost // 100

print("The cost of the call is: $" + dollars + "." + cents)
