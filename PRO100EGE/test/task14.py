def convert(n):
    pattern = ""
    while n:
        pattern += str(n % 4)
        n //= 4
    return pattern[::-1]


lst = []
for x in range(1, 3000):
    n = convert(4 ** 210 + 4 ** 110 - x)
    if str(n).count("0") == 105:
        print(x, n)
        break

# print(max(lst))
