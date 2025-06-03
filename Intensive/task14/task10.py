def convert(x, base):
    lst = []
    while x:
        lst = [x % base] + lst
        x //= base
    return lst


n = 43 * 7 ** 103 -21 * 7 ** 57 + 98
print(sum(convert(n, 7)))
