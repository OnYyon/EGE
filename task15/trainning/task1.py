def check(a):
    for x in range(1, 100500):
        f1 = x % 13 == 0
        f2 = x % 21 == 0
        f3 = x + a >= 500
        if ((f1 <= (not f2)) or f3) != 1:
            return False
    return True


for a in range(1, 10000):
    if check(a):
        print(a)
        break
