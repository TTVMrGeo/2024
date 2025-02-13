def nums(num):
  num, added = sorted(list(set(num.split(", ")))), 0
  for i in range(len(num)):
      if i % 2 != 0: added += int(num[i])
  print(added)

nums("1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 8, 9")