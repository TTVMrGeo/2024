def solution(number):
    a = 0
    if number / 3 > 0:
        a += 3
        number /= 3
    if number / 5 > 0:
        a += 5
        number /= 5
    return a