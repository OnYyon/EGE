def divs(x):
    ds = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


last_M = 0
lst = []
for x in range(710_017, 1000_000):
    ds = divs(x)
    if not ds: continue
    last = max(d for d in ds  if d < x ** 0.5)
    if last != 0:
        M = last + x // last
        if M > last_M and M % 10 == 0:
            lst.append((x, M))
            last_M = M
            if len(lst) == 5:
                break

for i in lst:
    print(*i)
