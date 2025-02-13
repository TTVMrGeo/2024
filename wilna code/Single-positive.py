def sp(a, b):
    if a > 0 and b < 0: return "YES"
    elif a < 0 and b > 0: return "YES"
    else: return "NO"
print(sp(int(input()), int(input())))