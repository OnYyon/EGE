def f(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 3
    return f(n - 1) - f(n - 2) + 2 * n


print(f(15))
