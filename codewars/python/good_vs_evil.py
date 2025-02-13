def good_vs_evil(good, evil):
    good, evil, good_total, evil_total, goods, evils = list(map(int, good.split(" "))), list(map(int, evil.split(" "))), 0, 0, [1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]
    try:
        for j in range(len(good)):
            for i in range(good[j]): good_total += goods[j]
        for j in range(len(evil)):
            for i in range(evils[j]): evil_total += evils[j]
    except(Exception):
        pass
    return "Battle Result: Good triumphs over Evil" if good_total > evil_total else "Battle Result: Evil eradicates all trace of Good" if evil_total > good_total else "Battle Result: No victor on this battle field"
print(good_vs_evil('1 1 1 1 1 1', '1 0 1 1 1 1 1'))

#! This is stupid