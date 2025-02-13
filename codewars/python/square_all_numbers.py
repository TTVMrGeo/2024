def square_digits(num):
    num = [int(x) for x in str(num)]
    num = [x**2 for x in num]
    num = [str(x) for x in num]
    num = ''.join(num)
    num = int(num)
    return(num)