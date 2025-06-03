from math import log2, ceil
symbol = ceil(log2(70))
user = 70 * 1024 / 2048
pas = ceil(24 * symbol / 8)
print(user - pas - 4)
