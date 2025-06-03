from itertools import combinations

print(len(list(combinations(range(11), r=3))) * 6 * 4 ** 8 - len(list(combinations(range(10), 3))) * 6 * 4 ** 7)
