def linear(l, n):
  n = str(n)
  l = list(l)
  a = 0
  for j in range (len(l)):
    if n in l:
      return True
    else:
      a += 1
  return False
print(linear(str(input()), int(input())))