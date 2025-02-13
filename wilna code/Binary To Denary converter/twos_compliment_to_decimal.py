def tb_to_d(binary_o):
    binary = list(binary_o[::-1])
    ans = 0

    if binary[0] == "1":
        ans += 1
    if binary[1] == "1":
        ans += 2
    if binary[2] == "1":
        ans += 4
    if binary[3] == "1":
        ans += 8
    if binary[4] == "1":
        ans += 16
    if binary[5] == "1":
        ans += 32
    if binary[6] == "1":
        ans += 64
    if binary[7] == "1":
        ans -= 128
            
    print(f"The two's compliment number: {binary_o} in decimal is: {ans}")