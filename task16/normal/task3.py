def f(n):
    if n == 1:
        return 6
    if n == 2:
        return 8
    if n == 3:
        return 100
    return 3 + 2 * f(n - 2)


print(f(13))
