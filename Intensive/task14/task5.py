for base in range(2, 1000):
    print(int("100", base), int("1000", base))
    if int("100", base) <= 70 < int("1000", base):
        # print(base, int("100", base), int("100", base))
        break
