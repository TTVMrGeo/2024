a = input()
a = a.lower().replace(" ", "")
b = a[::-1]

if a == b:
  print("The word is a Pallindrome!")
else:
  print("The word is not a Pallindrome!")