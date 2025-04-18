def cnt(start, end: int) -> int:
    lst = [0] * 101 * 2
    lst[start] = 1
    for i in range(start, end + 1):
        lst[i + 1] += lst[i]
        lst[i * 2] += lst[i]

    return lst[end]


print(cnt(4, 16) * cnt(16, 30) * cnt(30, 100))
