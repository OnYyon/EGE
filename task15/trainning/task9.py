def check(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 2 * x < a) or (x > 20) or (y > 30)) != 1:
                return 0
    return 1


for a in range(1, 1000):
    if check(a):
        print(a)
