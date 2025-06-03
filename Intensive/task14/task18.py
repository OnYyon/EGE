def convert(n: list, base: int):
    s = 0
    i = len(n) - 1
    for x in n:
        s += x * base ** i
        i -= 1
    return s


for x in range(67):
    n1 = convert([3, x, 2, 1], 81)
    n2 = convert([1, 7, x, 4], 67)
    if (n1 + n2) % 35 == 0:
        print((n1 + n2) // 35)
