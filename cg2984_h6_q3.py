#problem a
def rotate(s): 
  newString = " "
  for i in range(1, len(s)):
    newString+=s[i]
  newString+=s[0]
  return newString

#problem b
def rotate(s, n): 
  newString = " "
  for i in range(n, len(s)):
    newString+=s[i]
  for i in range(0, n):
    newString+=s[i]
  return newString

def main():
  string = input("Enter a string")
  num = int(input("Enter a number"))
  print(rotate(string, num))

main()
