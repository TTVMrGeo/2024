def to_camel_case(text):
    if "_" in text:
        text = text.replace("_", "-")
    text_lst = text.split("-")
    for j in range(len(text_lst)):
        if j == 0:
            pass
        else:
            text_lst[j] = text_lst[j].capitalize()
    output = "".join(text_lst)
    return output

print(to_camel_case("the-stealth_warrior"))