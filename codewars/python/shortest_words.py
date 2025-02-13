def find_short(s):
    words = s.split()

    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    return len(shortest_word)