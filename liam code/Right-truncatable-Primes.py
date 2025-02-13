final = []

def is_prime(num):
  for i in range(int(num)):
    if(i > 1 and (i != num)):
      if(int(num) % i == 0):
        return False
  return True

def is_Right_truncatable_prime(n):
  if str(n)[0] == '1':
    return False
  for i in range(len(str(n))):
    if not is_prime(n):
      return False
    n = str(n)[:-1]
  return True
    
def nth_Right_truncatable_prime(num):
  count = 0
  number = 1
  while count != num:
    if is_Right_truncatable_prime(number) == True:
      count += 1
      final.append(number)
    number += 1
    
  return number-1
  
print(nth_Right_truncatable_prime(int(input())))