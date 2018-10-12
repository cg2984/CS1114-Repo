n = int(input("Enter a number"))
aster = 2*(n-1)
space = 0
for i in range(0,n):
  print(space*" " + aster*"*" + space*" ")
  aster-=2
  space+=1
print("Done")


for i in range(0,n):
  space = (n-1)
  for i in range(0,n):
    print(space*" " + aster*"*" + space*" ")
    aster+=2
    space-=1
  print("Done")

