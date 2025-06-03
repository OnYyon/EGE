from itertools import product

lst = list(map("".join, product("ПАУК", repeat=4)))
print(len(list(filter(lambda x: "КА" not in x and "АК" not in x, lst))))