def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


cnt = 0
for x in range(32_500_000, 32_600_000):
    pr = [i for i in divs(x) if len(divs(i)) == 0]
    s = sum(pr)
    if s % 145 == 0 and s != 0:
        print(x, s)
        cnt += 1
        if cnt == 7:
            break
