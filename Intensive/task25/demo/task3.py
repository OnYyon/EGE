from fnmatch import fnmatch

for x in range(0, 10 ** 10, 18579):
    if fnmatch(str(x), "54?1?3*7"):
        print(x, x // 18579)

from itertools import product

# for a in range(10):
#     for b in range(10):
#         s = f"54{a}1{b}37"
#         x = int(s)
#         if x % 18539 == 0:
#             print(x, x // 18579)

for star_length in range(4):
    for a in range(10):
        for b in range(10):
            for star in product("0123456789", repeat=star_length):
                s = f"54{a}1{b}3{"".join(star)}7"
                x = int(s)
                if x % 18579 == 0:
                    print(x, x // 18579)
