def size_to_number(size):
    count = 0
    if "x" in size and "m" in size: return None
    size = list(size)
    while "x" in size:
        if size[0] == "x" and size[len(size) - 1] != "x":
            count += 1
            size.remove("x")
        else: return None
    if size == ['s']: return 36 - (2*count)
    if size == ['m']: return 38
    elif size == ['l']: return 40 + (2*count)
    else: return None

print(size_to_number(""))