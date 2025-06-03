from math import log2, ceil

for l in range(1000, -1, -1):
    symbol = ceil(log2(52 + 10 + 963))
    pas = ceil(l * symbol / 8)
    if pas * 2000 <= 693 * 1024:
        print(l)
        break
