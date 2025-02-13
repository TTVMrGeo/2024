def b_to_d(binary_o):
    binary = list(binary_o[::-1])
    a = 0
    b = 1
    ans = 0

    for binar in binary:
        if binary[a] == "1":
            ans += b
            a += 1
            b *= 2
            
        elif binary[a] == "0":
            ans += 0
            a += 1
            b *= 2