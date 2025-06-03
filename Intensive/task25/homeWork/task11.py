def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)

cnt = 0
for x in range(39345679-1, -1, -1):
    ds = divs(x)
    if len({2, 3, 5, 7} & set(ds)) == 4 and 76 <= len(ds) < 88:
        print(x, len(ds))
        cnt += 1
        if cnt == 10:
            break
