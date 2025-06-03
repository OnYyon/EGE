def f1(n):
    if n > 30:
        return 0
    if n == 30:
        return 1
    return f1(n + 1) + f1(n * 5)

def f2(n):
    if n > 68:
        return 0
    if n == 68:
        return 1
    return f2(n + 1) + f2(n * 5)


print(f1(3) * f2(30))
