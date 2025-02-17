def check(a):
    for x in range(1, 100500):
        f1 =  x & 49 == 0
        f2 = x & 33 == 0
        f3 = x & a == 0
        if ((not f1) <= (f2 <= (not f3))) != 1:
            return False
    return True


for a in range(1, 100500):
    if check(a):
        print(a)
        break
