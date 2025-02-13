def digital_root(n):
    ans = 0
    no_split = [n]
    splitd = list(map(int, str(no_split[0])))
    for j in range(len(splitd)):
        ans += splitd[j]
    while len(str(ans)) != 1:
        no_split = [ans]
        ans = 0
        splitd = list(map(int,str(no_split[0])))
        for j in range(len(splitd)):
            ans += splitd[j]
    return ans
       
print(digital_root(493193))