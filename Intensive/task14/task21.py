def convert(st, base):
    lst = []
    while st:
        lst = [st % base] + lst
        st //= base
    return lst


print(convert(7 ** 500 + 7 ** 200, 7).count(1))