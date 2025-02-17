def check(a):
    for x in range(1000):
        for y in range(1000):
            if ((x < a) and (y < a) and (x * y > 601)) != 0:
                return False
    return True


for a in range(1000):
    if check(a):
        print(a)
