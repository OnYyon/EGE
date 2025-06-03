def check(a):
    for x in range(1, 100500):
        f1 = x & 13 == 0
        f2 = x & 40 != 0
        f3 = x & a != 0
        if (f1 <= (f2 <= f3)) != 1:
            return 0
    return 1


for a in range(1, 100500):
    if check(a):
        print(a)
        break
