from itertools import permutations

lst = list(map("".join, permutations(sorted("ВИКТОР"))))
print(lst[265])
