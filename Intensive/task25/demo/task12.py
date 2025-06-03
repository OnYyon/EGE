def divs(x):
    ds = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)

def prime_divs(x):
    i = 2
    lst = []
    while i * i <= x:
        if x % i == 0:
            lst.append(i)
            x //= i
        else:
            i += 1
    if x > 1:
         lst.append(x)
    return lst


cnt = 0
for x in range(55_000_000, 60_000_000):
    prdivs = prime_divs(x)
    pr777 = [d for d in prdivs if d % 1000 == 777]

    if pr777:
        print(x, min(pr777), prdivs)
        cnt += 1
        if cnt == 4:
            break

print()
cnt = 0
for x in range(55_000_000, 60_000_000):
    ds = divs(x)
    if not ds: continue
    pr777 = [d for d in ds if d % 1000 == 777 and
                                        len(divs(d)) == 0]
    if pr777:
        print(x, min(pr777), ds)
        cnt += 1
        if cnt == 4:
            break

