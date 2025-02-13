def duplicate_count(text):
    text = text.lower()
    past = []
    rejected = []
    rejected_not = []
    for j in range(len(text)):
        if text[j] not in past: past.append(text[j])
        else: rejected.append(text[j])
    for i in rejected:
        if i not in rejected_not: rejected_not.append(i)
    return len(rejected_not)

print(duplicate_count("Indivisibilities"))