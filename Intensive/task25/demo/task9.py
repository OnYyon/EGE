from fnmatch import fnmatch


def divs(x):
    ds = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


for x in range(400_000, 500_001):
    lst = [d for d in divs(x) if fnmatch(str(d), "*7?")]
    if len(lst) >= 18:
        print(x, sum(lst))
