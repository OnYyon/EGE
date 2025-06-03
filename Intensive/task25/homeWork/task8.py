def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


cnt = 0
for x in range(310_000+1, 500_000):
    dp = [i for i in divs(x) if len(divs(i)) == 0]
    if not dp: continue
    a = sum(dp) // len(dp)
    if a % 6 == 0 and a % 10 != 4:
        print(x, a)
        cnt += 1
        if cnt == 6:
            break
