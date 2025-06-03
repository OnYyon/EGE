def convert(x, n):
    lst = []
    while x:
        lst = [x % n] + lst
        x //= n
    return lst

o = []
for x in range(1000):
    n = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** x - 2022
    if n <= 0:
        break
    o.append(sum(convert(n, 4)))

print(len(set(o)))
