from itertools import product

lst = list(map("".join, product(sorted("АБВ"), repeat=5)))
print(lst[239])
