def check(a):
    for x in range(100000):
        f = lambda m, n: m % n == 0
        f1 = f(x, a)
        f2 = f(x, 16)
        f3 = f(x ,23)
        if ((f1 and not(f2)) <= f3) != 1:
            return False
    return True


for i in range(1, 1000000):
    if check(i):
        print(i)
