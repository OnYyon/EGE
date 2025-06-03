def convert(n):
    pattern = ""
    while n:
        pattern += str(n % 3)
        n //= 3
    return pattern[::-1]


lst = []
for n in range(3, 1000):
    r = convert(n)
    if n % 3 == 0:
        r += "12"
    else:
        r += convert((n % 3) * 3)
    if int(r, 3) < 150:
        lst.append(n)
print(max(lst))
