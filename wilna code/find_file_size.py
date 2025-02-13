hor = int(input("Horizontal Pixels > "))
ver = int(input("Vertical Pixels > "))
pixels = hor * ver
bit_depth = int(input("Bit depth > "))
byte_size = (pixels * bit_depth)/8
kilobyte_size = byte_size/1000
print(f"{byte_size} Bites")
print(f"{kilobyte_size} Kilobytes")