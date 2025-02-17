def check(a):
    for x in range(1, 100000):
        f1 = (x % 6 == 0)
        f2 = (x % 10 == 0)
        f3 = ((x + a) > 121)
        if ((f1 <= (not f2)) or f3) != 1:
            return False
    return True


for i in range(1, 10000):
    if check(i):
        print(i)
        break

