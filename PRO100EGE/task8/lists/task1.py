from itertools import product

lst = list(map("".join, product(sorted("БАТЫР"), repeat=5)))
for i, v in enumerate(lst):
    if "Ы" not in v and "АА" not in v:
        print(i, v)
        break
