from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(9999)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n * f(n - 2)


print(f(2023) // f(2019))
