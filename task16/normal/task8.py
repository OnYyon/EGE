from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    return n + f(n + 2)


for i in range(2025, 1, -1):
    f(i)

print(f(2022) - f(2023))
