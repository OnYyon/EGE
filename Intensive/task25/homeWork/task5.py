from itertools import product, repeat

lst = []
for l in range(3):
    lst += ["".join(x) for x in product("123456789", repeat=l)]

lst2 = []
for l in range(3):
    lst2 += ["".join(x) for x in product("0123456789", repeat=l)]

for a in lst:
    for b in lst2:
        if len(a) + len(b) > 2:
            break
        p = int(f"{a}15{b}7424")
        ds = [111, 113, 127]
        flag = [p % i == 0 for i in ds]
        if flag.count(True) == 1:
            print(p, p // ds[flag.index(True)])
