from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 2:
        return 5
    if n > 2:
        return n + f(n - 2)

for i in range(2, 686868, 2):
    f(i)

print(f(686868) - f(686800))
