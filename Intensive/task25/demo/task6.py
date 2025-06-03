def div(x):
    dv = set() # can be modified
    for d in range(2, int(x ** .5) + 1):
        if x % d == 0:
            # x // d, то что больше >корня
            # d то что <корня
            dv |= {d, x // d}
    return sorted(dv)

lst = []
for x in range(500_000, 1000_000):
    r = sum(div(x))
    if r % 10 == 9:
        lst.append((x, r))
        if len(lst) == 5:
            break

for i in lst:
    print(*i)
