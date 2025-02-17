def check(a):
    for x in range(1000):
        for y in range(1000):
            f1 = x * y > a
            f2 = x > y
            f3 = x < 8
            f = f1 and f2 and f3
            if f != 0:
                return False
    return True


for i in range(10000):
    if check(i):
        print(i)
        break