from math import log2, ceil

symbol = ceil(log2(5000))
password = ceil(101 * symbol / 8)
print(password * 2048 / 1024)
