def convert(st, base):
    lst = []
    while st:
        lst = [st % base] + lst
        st //= base
    return lst


for x in range(1000):
    if sum(convert(36 ** 17 - 6 ** x + 71, 6)) == 61:
        print(x)
        break
