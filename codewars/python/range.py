def range_function(a, b = None, c = None):
        num = 1
        final = []
        if b != None and c == None:
            c = b
            b = None
        if c == None:
            if b == None:
                while not num >= (a + 1):
                    final.append(num)
                    num += 1
            else:
                    while not num >= (a + 1):
                        final.append(num)
                        num += b
        else:
            num = a
            if b == None:
                while not num >= (c + 1):
                    final.append(num)
                    num += 1
            else:
                    while not num >= (c + 1):
                        final.append(num)
                        num += b
        return final