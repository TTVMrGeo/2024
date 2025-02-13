def string_to_ascii(string):
    asciis = [ord(c) for c in string]
    hexs = []
    for j in range(len(asciis)):
        hexs.append(hex(asciis[j]))
    print(str(hexs).replace("[", "").replace("]", "").replace("0x", "").replace("'", "").replace(",", ""))
    
string_to_ascii("Big Boi")