def rgb(r, g, b): return "{:02X}{:02X}{:02X}".format(0 if r < 0 else 255 if r > 255 else r, 0 if g < 0 else 255 if g > 255 else g, 0 if b < 0 else 255 if b > 255 else b)
print(rgb(-20, 275, 125))