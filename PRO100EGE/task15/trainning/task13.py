def check(a):
    for x in range(100000):
        for y in range(100000):
            if ((x + 2 * y > 48) or (y > x) or (x + 3 * y < a)) == 0:
                return 1


for a in range(100000):
    if check(a):
        print(a)
