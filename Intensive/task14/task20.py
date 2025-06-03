def convert(st, base):
    lst = []
    while st:
        lst = [st % base] + lst
        st //= base
    return lst



print(convert(abs(3*5**1984 - 7*25**777 - 11*125**666 - 404), 5).count(2))