def convert(n: list):
    s = 0
    i = len(n) - 1
    for x in n:
        s += x * 37 ** i
        i -= 1
    return s


for x in range(37):
    n1 = convert([12, 5, 9, x, 11, 10, 9, 8, 15])
    n2 = convert([14, 3, x, 5, 13, 10, 9, 12, 6])
    if (n1 * n2) % 36 == 0:
        print(convert([2, x, 1]))
