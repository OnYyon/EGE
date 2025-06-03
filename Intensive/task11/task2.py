from math import log2, ceil

l = 15
symbol = ceil(log2(8))
additional = 24
password = ceil(l * symbol / 8)
user = password + additional
print(user * 20)
