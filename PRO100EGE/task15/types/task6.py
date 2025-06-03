def check(a):
    for x in range(1, 100500):
        x_13 = x & 13 != 0
        x_39 = x & 39 == 0
        x_a = x & a == 0
        f = ((x_13 or x_39) <= x_13) or (x_a and (not x_13))
        if f != 1:
            return False
    return True


for i in range(1, 100500):
    if check(i):
        print(i)
