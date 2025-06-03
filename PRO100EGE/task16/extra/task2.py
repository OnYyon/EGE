from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 4
    return n + f(n - 2)


for i in range(1, 10001, 2):
    f(i)

print(f(10001) + f(13))
