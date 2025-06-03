def convert(x, base):
    lst = []
    while x:
        lst = [x % base] + lst
        x //= base
    return lst



n = 7 ** 202 + 49 ** 102 - 7 ** 20
print(convert(n, 7).count(6))
