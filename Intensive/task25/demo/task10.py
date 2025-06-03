def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


for i in range(326496, 649633):
    d = divs(i)
    ch = list(filter(lambda x: x % 2 == 0, d))
    nch = list(filter(lambda x: x % 2 != 0, d))
    if len(ch) == len(nch) and len(d) >= 140:
        print(i, min(filter(lambda x: x > 1000, d)))
