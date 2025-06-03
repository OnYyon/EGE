from math import log2, ceil

l = 1231
for i in range(1, 10000):
    symbol = ceil(log2(i))
    pas = ceil(l * symbol / 8)
    if pas * 523872 > 432 * 1024 * 1024:
        print(i)
        break
