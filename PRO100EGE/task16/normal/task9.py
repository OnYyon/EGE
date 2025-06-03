from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 20000:
        return 1
    return n + f(n + 4)


# Разгон буфера lru_cashe
for i in range(20000, 1, -1):
    f(i)

print(f(1) + f(2023))
