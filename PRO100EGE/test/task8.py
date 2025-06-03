from itertools import product

lst = list(map("".join, product(sorted("ПОБЕДА"), repeat=6)))
for i in range(len(lst) - 1, -1, -1):
    if (i + 1) % 2 == 0 and lst[i][0] == "О" and len(set(lst[i])) == len(lst[i]):
        print(lst[i], i)
        break
