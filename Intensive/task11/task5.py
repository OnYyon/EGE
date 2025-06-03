from math import log2, ceil
l = 295
l = l -1
symbol = ceil(log2(4560))
pas = ceil(symbol * l / 8)
print(pas * 131072 / 1024)
