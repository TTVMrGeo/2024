def count_repeats(txt):
    txt_lst = [*txt]
    current = ""
    count = 0
    for j in range(len(txt_lst)):
        current = txt_lst[j]
        try:
            if current != txt_lst[j+1]: pass
            else: count += 1
        except Exception: pass
    return count
        
print(count_repeats('abbbbc'))