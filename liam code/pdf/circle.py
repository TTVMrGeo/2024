x, y = map(float, input().split(" "))
print("BLUE" if ((x**2 + y**2)**0.5 > 1) else "RED")