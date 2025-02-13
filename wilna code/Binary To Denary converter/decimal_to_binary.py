def btod(n):
    a = 128
    ans = []
    while a > 0:
        if n >= a:
            ans.append(1)
            n -= a
        else:
            ans.append(0)
        a = a // 2
    return str(ans).replace('[','').replace(']','').replace(',','').replace(' ','')
            
print(btod(int(input())))