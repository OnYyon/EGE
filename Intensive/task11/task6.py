from math import log2, ceil
l = 317
symbol = ceil(log2(4100))
pas = ceil(l * symbol / 8)
print(pas * 262144 / 1024 / 1024)
