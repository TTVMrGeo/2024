def bingo(ticket,win):
    a = -1
    b = -1
    c = 0
    for j in range(len(ticket)):
        a += 1
        b += 1
        c += 1
        return True if ord([*ticket[a][0]][b]) == ticket[b][c] else False

print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2))