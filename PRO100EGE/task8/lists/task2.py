from itertools import product

lst = list(map("".join, product(sorted("АБЗИ"), repeat=4)))
print(lst.index("ИЗБА"))
