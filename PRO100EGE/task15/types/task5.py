def check(a):
    for x in range(1, 100500):
        x_42 = x & 42 != 0
        x_34 = x & 34 == 0
        x_a = x & a == 0
        f = (x_42 and x_34) <= (not x_a)
        if f != 1:
            return False
    return True


for i in range(1, 100500):
    if check(i):
        print(i)
        break
