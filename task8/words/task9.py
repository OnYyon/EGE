from itertools import product

lst = list(map("".join, product("ПАУК", repeat=5)))
print(len(list(filter(lambda x: "КК" not in x, lst))))
