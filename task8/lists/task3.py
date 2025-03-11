from itertools import product

lst = list(map("".join, product(sorted("ЛЕМУР"), repeat=4)))
for i, v in enumerate(lst):
    if v[0] == "Л":
        print(i, v)
        break
