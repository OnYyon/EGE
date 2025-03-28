def check(a):
    for x in range(100500):
        f1 = x % a == 0
        f2 = x % 21 == 0
        f3 = x % 35 == 0
        if (f1 <= ((not f2) or f3)) != 1:
            return 0
    return 1

for a in range(1, 100500):
    if check(a):
        print(a)
        break
