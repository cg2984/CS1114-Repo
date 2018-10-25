def rotate(s): 
  newString = " "
  for i in range(1, len(s)):
    newString+=s[i]
  newString+=s[0]
  return newString

def main():
  string = input("Enter a string")
  print(rotate(string))
main()
