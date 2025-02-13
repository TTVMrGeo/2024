def repeat(a, b):
    n = a
    deficients = 0
    perfects = 0
    abundants = 0
    while not n > b:
        ans = 0

        def find_divisors(num): 
            divisors = [] 
            for i in range(1, num+1): 
                if num % i == 0:
                    if i != num:
                        divisors.append(i) 
            return divisors 

        divs = find_divisors(n)

        for j in range(len(divs)):
            ans += divs[j]

        if ans < n:
            deficients += 1
        if ans == n:
            perfects += 1
        if ans > n:
            abundants += 1
        n += 1
    return f"{deficients} {perfects} {abundants}"

a, b = map(int, input().split(" "))
print(repeat(a, b))