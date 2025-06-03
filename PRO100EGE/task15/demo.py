def check(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 4 * x != 120) or ((x > a) or (y > a))) != 1:
                return 0
    return 1


for a in range(0, 1000):
    if check(a):
        print(a)
