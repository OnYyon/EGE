def convert(n: list, base: int):
    s = 0
    i = len(n) - 1
    for x in n:
        s += x * base ** i
        i -= 1
    return s



for p in range(10, 10000):
    for x in range(p):
        for y in range(p):
            a = convert([5, x, 8, 3], p) + convert([x, 9, x, 9], p)
            b = convert([y, 2, 0, y], p)
            if a == b:
                print(convert([x, y, y, x], p))
                break
