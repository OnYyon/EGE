def check(a):
    for x in range(100000):
        f1 = (x % a == 0)
        f24 = (x % 24 == 0)
        f3 = (x % 16 == 0)
        if ((not(f1) and f24) <= (not(f3) or not(f24))) != 1:
            return False
    return True


for i in range(1, 10000):
    if check(i):
        print(i)
