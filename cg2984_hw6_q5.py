#Clara Gilligan
#Homework 6
#CS 1114
#10/30/18

def sum_range(s, e):
    total = s
    for i in range(s+1,e+1):
        total+=i
    print(total)
def main():
    start = int(input("Enter a starting number: "))
    end = int(input("Enter an ending number: "))
    sum_range(start,end)
main()
