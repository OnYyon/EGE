def f(n):
    if n == 1:
        return 3
    if n == 2:
        return 1
    return 68 + f(n - 2)


print(f(13))
