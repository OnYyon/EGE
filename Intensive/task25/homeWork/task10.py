import fnmatch


def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


lst = []
for x in range(10**6):
    ds = divs(x)
    d = [t for t in ds if str(t)[0] == "4"]
    if len(d) == 24:
        print(x, ds[-1])
