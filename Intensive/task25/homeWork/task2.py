from itertools import product

lst = []
for i in range(5):
    lst += ["".join(t) for t in (product("0123456789", repeat=i))]

s = set()
for a in lst:
    for b in lst:
        if len(a) + len(b) > 5:
            break
        x = f"1{a}5{b}{9}"
        if int(x) % 21 == 0 and all(a < b for a, b in zip(x, x[1:])):
            s |= {int(x)}

for i in sorted(s):
    print(i, i // 21)
