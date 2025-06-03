from itertools import product

lst = list(map("".join, product("РУСТАМ", repeat=6)))
lst = [i for i in lst if (t := i.count('Р') + i.count('С') + i.count('Т') + i.count('М')) and t >= 3]
print(lst, len(lst), sep="\n")
