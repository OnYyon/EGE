from math import log2, ceil
l = 19
symbol = ceil(log2(15))
pas = ceil(symbol * l / 8)
user = pas + 36
print(user * 8192 / 1024)