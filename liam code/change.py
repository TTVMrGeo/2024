x, money, change = int(input()), [200,100,50,20,10,5,2,1], [0, 0, 0, 0, 0, 0, 0, 0]
for j, i in enumerate(money):
    if i <= x and x > 0:
        change[j] += x//i
        x -= i*(x//i)
print(" ".join(str(i) for i in change[::-1]))