from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n + f(n - 1)


for i in range(1, 4068):
    f(i)

print(f(4068) - f(4066))
