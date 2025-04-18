def cnt(start, end):
    lst = [0] * 151 * 4
    lst[start] = 1
    for i in range(start, end + 1):
        lst[i + 1] += lst[i]
        lst[i * 4] += lst[i]
    return lst[end]


print(cnt(4, 20) * cnt(20, 150))
