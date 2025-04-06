from functools import lru_cache


@lru_cache()
def f(n):
    if n == 30:
        return 1
    if n < 30:
        return 0
    return f(n - 1) + f(n - 2) + f(n - 3)


print(f(68))
