def check(a):
    for x in range(1, 100500):
        f1 = x % 15 == 0
        f2 = x % 24 == 0
        f3 = x % a == 0
        if ((f1 and (not f2)) <= (not f3 or not f1)) != 1:
            return False
    return True


for a in range(1, 100500):
    if check(a):
        print(a)
        break
