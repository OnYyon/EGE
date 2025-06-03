def summore(s, d):
    return s + d > 0


def check(a):
    for x in range(1, 10000):
        f1 = x + a >= 160
        f2 = x % 7 == 0
        f3 = summore(x, -17)
        if (f1 or (f2 <= (not f3))) != 1:
            return False
    return True


for i in range(1, 10000):
    if check(i):
        print(i)
        break
