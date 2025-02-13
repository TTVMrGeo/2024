def make_readable(seconds):
    h = 0
    m = 0
    s = 0
    while seconds > 59:
        seconds -= 60
        m += 1
    s = seconds
    while m > 59:
        h += 1
        m -= 60
    if h < 10: h = f"0{h}"
    if m < 10: m = f"0{m}"
    if s < 10: s = f"0{s}"
    return f"{h}:{m}:{s}"
print(make_readable(69))