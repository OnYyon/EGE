from itertools import product

lst = list(map("".join, product(sorted("ЛАЙМ"), repeat=5)))
cnt = 0
for i in range(len(lst) - 1, -1, -1):
    if "Л" not in lst[i] and "М" not in lst[i] and "ЙЙ" not in lst[i]:
        print(i, lst[i])
        break
