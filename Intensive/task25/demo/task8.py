def divs(x):
    ds = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)

lst = []
for i in range(800_001, 1000_000):
    d = divs(i)
    if not d: continue
    m = d[0] + d[-1]
    if m % 10 == 4:
        lst.append((i, m))
        if len(lst) == 5:
            break

for i in lst:
    print(*i)
