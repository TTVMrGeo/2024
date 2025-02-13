def padovan(n):
    twoPrev, prev, current, next = 1, 1, 1, 1
    
    for i in range(3, n+1):
        next = twoPrev + prev
        twoPrev = prev
        prev = current
        current = next
 
    return next
        
print(padovan(10000))