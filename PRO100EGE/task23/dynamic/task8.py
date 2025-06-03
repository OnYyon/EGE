# I think this is best practice in EGE
def cnt(start, end):
    lst = [0] * end * 2
    lst[start] = 1
    for i in range(start + 2, end + 1):
        lst[i] += lst[i - 2]
        if i % 3 == 0:
            lst[i] += lst[i // 3]
    return lst[end]
print(cnt(3, 19) * cnt(19, 91))
