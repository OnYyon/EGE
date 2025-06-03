from math import log2, ceil

l = 23
for i in range(100000, -1, -1):
    symbol = ceil(log2(i))
    pas = ceil(symbol * l / 8)
    if pas * 500_000 <= 21 * 1024 * 1024:
        print(i)
        break
