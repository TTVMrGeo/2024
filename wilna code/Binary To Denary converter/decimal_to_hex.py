def d_to_h(decimal):
    hex_string = ''
    hex_digits = '0123456789ABCDEF'
    
    if decimal == 0:
        hex_string = '0'
    
    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_digits[remainder] + hex_string
        decimal = decimal // 16
    
    print(hex_string)
d_to_h(int(input()))