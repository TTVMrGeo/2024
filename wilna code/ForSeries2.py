a = int(input()); b = int(input()); ans = ""
if a > b:
    while a != (b - 1): ans = ans + str(a) + " "; a -= 1
elif a < b:
    while a != (b + 1): ans = ans + str(a) + " "; a += 1
else:
    print(a or b)
    exit()
print(ans)