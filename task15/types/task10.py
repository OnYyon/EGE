def pos(n, m):
    return n - m > 0


def check(a):
    for x in range(1000):
        for y in range(1000):
            f1 = pos(x + y, 73)
            f2 = pos(37, x-y)
            f3 = pos(y, a)
            if (not f1 or not f2 or f3) == 0:
                return False
    return True


lst = []
for i in range(100000):
    if check(i):
        lst.append(i)
        print(lst)
