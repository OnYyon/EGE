from itertools import product

lst = list(map("".join, product(sorted("СЕНТЯБРЬ"), repeat=5)))
for i in range(len(lst) - 1, -1, -1):
    if lst[i][0] == "Р" and "Ь" not in lst[i] and i % 2 != 0:
        print(i, lst[i])
        break
