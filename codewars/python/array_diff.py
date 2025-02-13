def array_diff(a, b):
    if len(b) < 1: return a
    for j in range(len(b)):
        while b[j] in a: a.remove(b[j])
    return a

print(array_diff([1,2,3], [1, 2]))