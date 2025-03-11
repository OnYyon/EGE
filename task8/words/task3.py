from itertools import product

lst = list(map("".join, product("БАНКИР", repeat=6)))
lst = [i for i in lst if 0 <= i.count("А") <= 1 and 0 <= i.count("И") <= 1]
print(lst, len(lst), sep="\n")
