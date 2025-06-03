from itertools import product

lst = list(map("".join, product("АОУ", repeat=5)))
cnt = 0
start = False
for i in lst:
    if i == "ОУОУА":
        start = True
    if start:
        cnt += 1
    if i == "УАУАУ":
        start = False
print(cnt)
