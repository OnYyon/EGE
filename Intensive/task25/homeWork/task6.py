def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


for x in range(224466, 664422 + 1):
    ds = divs(x)
    if not ds: continue
    if max(ds) % 100 == 19:
        if len({5, 7, 13} & set(ds)) == 3 and len({25, 49, 169} & set(ds)) == 0 and max(ds) <= 100_000:
            print(x, max(ds))
