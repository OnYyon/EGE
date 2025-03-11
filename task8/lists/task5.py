from itertools import product

lst = list(map("".join, product(sorted("ФОКУС"), repeat=5)))
for i in range(len(lst) - 1, -1, -1):
    if lst[i].count("Ф") == 0 and lst[i].count("У") == 2:
        print(i, lst[i])
        break
