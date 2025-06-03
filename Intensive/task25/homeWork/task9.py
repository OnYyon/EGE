def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


for i in range(112_500_000, 112_550_000 + 1):
    m = sum(divs(i)[-2:])
    if m % 10000 == 1214:
        print(i)