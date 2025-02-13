inpts = str(input()).upper()
inpts_lst = []
final = []
a = 0
output = ""
counter = 0

for j in range(len(inpts)):
    inpts_lst.append(inpts[:1])
    inpts = inpts[::-1]
    inpts = inpts[:-1]
    inpts = inpts[::-1]

while counter < len(inpts_lst):
    try:
        if inpts_lst[a] == inpts_lst[a+1]:
            inpts_lst.remove(inpts_lst[a])
            if f"S{inpts_lst[a-1]}" != f"S{inpts_lst[a]}":
                final.append(f"S{inpts_lst[a]}")
        else:
            if inpts_lst[a] not in inpts_lst[a-1]:
                final.append(inpts_lst[a])
        a += 1
    except Exception:
        final.append(inpts_lst[a])
        
    counter += 1
    
output = "".join(final)
    
print(output)