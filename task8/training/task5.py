from itertools import product

lst = list(map("".join, product(sorted("КОМПЬЮТЕР"), repeat=5)))
for i in range(len(lst) - 1, -1, -1):
    if (i + 1) % 2 == 1 and lst[i][0] != "Ь" and lst[i].count("К") == 2:
        print(lst[i], i)
        break
