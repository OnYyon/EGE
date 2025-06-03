# 1?2*0*2?1
from itertools import product, repeat


def divs(x):
    ds = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


lst = []
for l in range(4):
    lst += ["".join(i) for i in product("0123456789", repeat=l)]

for a in range(10):
    for b in lst:
        for c in lst:
            for d in range(10):
                if len(b) + len(c) > 3: break
                x = int(f"1{a}2{b}0{c}2{d}1")
                ds = divs(x)
                if len(ds) == 3:
                    print(x)
