def move_zeros(lst):
    a = lst.count(0)
    while 0 in lst: lst.remove(0)
    for j in range(a): lst.append(0)
    return lst