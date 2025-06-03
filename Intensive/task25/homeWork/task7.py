def divs(x):
    ds = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)


cnt = 0
for i in range(1_125_000, 1_500_000):
    ds = divs(i)
    lst7 = list(filter(lambda x: x % 10 == 7 and x != 7, ds))
    if not lst7: continue
    if len(lst7) > 0:
        print(i, lst7[0])
        cnt += 1
        if cnt == 5:
            break
