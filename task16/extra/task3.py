from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 10000:
        return 1
    return n + f(n + 2)


for i in range(10000, 1, -2):
    print(i)
    f(i)

print(f(1000) + f(10))
