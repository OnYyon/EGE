def check(a):
    for x in range(1, 100500):
        x_2 = x % 2 == 0
        x_3 = x % 3 == 0
        x_a = x + a >= 80
        f = (x_2 <= (not x_3)) or x_a
        if f != 1:
            return False
    return True


for i in range(1, 100500):
    if check(i):
        print(i)
        break