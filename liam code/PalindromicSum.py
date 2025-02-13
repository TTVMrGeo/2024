def flip_and_add(num):
    return num + int(str(num)[::-1])

def flip_is_num(fn):
    if fn == int(str(fn)[::-1]):
        return True
    else:
        return False
    
def is_palindromic_sum(s):
    a = 0
    while not flip_is_num(s):
        s = flip_and_add(s)
        a += 1
    return f"It took {a} steps."
        

asd = int(input())
print(is_palindromic_sum(asd))