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

#problem c
def all_rotations(s):
    newWord = " "
    for i in range(len(s)):
        newWord = rotate(s, i)
        print(newWord)
    
def main():
  string = input("Enter a string: ")
  all_rotations(string)

main()
