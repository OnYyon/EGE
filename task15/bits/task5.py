def check(a):
    for x in range(100500):
        f1 = x & 25 == 0
        f2 = x & 17 == 0
        f3 = x & a == 0
        if ((not f1) <= (f2 <= (not f3))) != 1:
            return 0
    return 1


for a in range(100500):
    if check(a):
        print(a)
        break
