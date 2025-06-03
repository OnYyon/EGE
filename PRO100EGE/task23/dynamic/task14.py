def cnt(start, end, n: int):
    lst = [0] * (end + 1) * 3
    lst[start] = 1
    for i in range(start, end + 1):
        lst[n] = 0
        lst[i + 1] += lst[i]
        lst[i * 2] += lst[i]
        lst[i * 3] += lst[i]
    return lst[end]


print(cnt(2, 15, 0) * cnt(15, 30, 0))
