name, score = str(input()).lower(), 0
for i in range(len([*name])): score += 5 if [*name][i] in [*"aeiou"] else 5 if [*name][i] in [*"bcdfg"] else 2
print("Slow" if score < 25 else "Medium" if score >= 25 and score <= 35 else "Fast")