from functools import lru_cache


@lru_cache(None)
def f(x, end):
    if x > end or x == 56:
        return 0
    if x == end:
        return 1
    return f(x + 3, end) + f(x + 7, end) + f(x * 3, end)

print(f(12, 40) * f(40, 72) * f(72, 89))
