from itertools import product

lst = list(map("".join, product("ВИШНЯ", repeat=4)))
cnt = 0
for i in lst:
    if i.count("В") >= 1 and i[0] != "Ш" and i[-1] not in "ИЯ":
        print(i)
        cnt += 1
print(cnt)
