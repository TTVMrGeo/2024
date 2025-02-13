# number = input()
# list_of_digits = list(map(int, str(number)))
# a = list_of_digits[0]
# b = list_of_digits[1]
# c = list_of_digits[2]

# if a < b < c:
#     print("YES")
# else:
#     print("NO")
    
number = input()
a = number[0]
b = number[1]
c = number[2]

if a < b < c:
    print("YES")
else:
    print("NO")