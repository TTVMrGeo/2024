from binary_to_decimal import b_to_d; from twos_compliment_to_decimal import tb_to_d; from decimal_to_hex import d_to_h

a = input("Would you like to:\nA) Convert from binary to decimal\nB) Convert from two's compliment binary to decimal\nC) Convert from decimal to hexadecimal\n> ")

if a == "a" or a == "A":
    b_to_d(input())
elif a == "b" or a == "B":
    tb_to_d(input())
elif a == "c" or a == "C":
    d_to_h(int(input()))
else:
    print("That wasn't an option!")