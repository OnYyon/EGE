def divs(x):
    ds = {1, }
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
    return sorted(ds)

lst = []
for x in range(770000, -1, -1):
    d = divs(x)[:-1]
    a = sum(d) // len(d)
    if a % 100 == 12:
        lst.append((x, a))
        if len(lst) == 5:
            break

for i in lst:
    print(*i)
