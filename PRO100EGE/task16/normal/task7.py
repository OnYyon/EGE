from functools import *


@lru_cache(None)
def f(n):
    if n <= 2:
        return n
    if n > 2:
        return n + f(n - 2)


for i in range(1, 2023, 1):
    f(i)

print(f(2023) + f(2020))
