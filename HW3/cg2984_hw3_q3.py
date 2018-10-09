#Clara Gilligan
#9/29/18
#Homework 3
#CS 1114

import math

callCost = 0
small_rate = 0.15
medium_rate = 0.25
large_rate = 0.40

callDay = input("Please enter the first three letters of the day the call started: ")
callTime = int(input("Please enter the time of the call (hhmm): "))
callDuration = int(input("Please enter the duration of the call in minutes: "))

if callDay == "Sat" or "Sun":
  callCost = callDuration * small_rate
elif callDay == "Mon" or "Tue" or "Wed" or "Thu" or "Fri": 
  if callTime > 800 or callTime < 1800:
    callCost == callDuration * large_rate
  elif callTime < 800 or callTime > 1800:
    callCost == callDuration * medium_rate
else:
    print("Something has gone wrong")

print("The cost of the call is: $" + str(callCost))
