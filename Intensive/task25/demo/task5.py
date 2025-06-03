from fnmatch import fnmatch

# for i in range(447361, 10**10):
#     if fnmatch(str(i), "4*4736*1") and i % 7993 == 0:
#         print(i)
#         break

# for x in range(44736821, 10 ** 10, 7993):
#     if fnmatch(str(x), "4*4736*1"):
#         print(x, x // 7993)

from itertools import product

lst = []
for l in range(5):
    lst += ["".join(x) for x in product("0123456789", repeat=l)]


h = []
for a in lst:
    for b in lst:
        if len(a) + len(b) > 4:
            break
        x = int(f"4{a}4736{b}1")
        if x % 7993 == 0:
            h.append(x)

for item in sorted(h):
    print(item, item // 7993)
