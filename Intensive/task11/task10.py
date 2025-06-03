from math import log2, ceil

l = 303
symbol = ceil(log2(8200))
pas = ceil(l * symbol / 8)
for a in range(100000, -1, -1):
    user = pas + a
    if user * 101 <= 101 * 1024:
        print(a)
        break
