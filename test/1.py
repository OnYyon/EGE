def f1(n):
    if n > 5:
        return 0
    if n == 5:
        return 1
    return f1(n + 1) + f1(n + 2) + f1(n * 3)


def f2(n):
    if n > 21 or n == 8 or n == 11:
        return 0
    if n == 21:
        return 1
    return f2(n + 1) + f2(n + 2) + f2(n * 3)


print(f1(2) * f2(5))
