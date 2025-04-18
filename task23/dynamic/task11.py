import time

# Best
start = time.time()
lst = [0] * 71 * 4
lst[2] = 1
for i in range(2, 71):
    lst[35] = 0
    lst[i + 1] += lst[i]
    lst[i * 3] += lst[i]
    lst[i * 4] += lst[i]
end = time.time()
print(lst[70], end - start)


# Better, but not best
def cnt(start, end: int) -> int:
    lst = [0] * 71 * 4
    lst[start] = 1
    for i in range(start, end + 1):
        lst[i + 1] += lst[i]
        lst[i * 3] += lst[i]
        lst[i * 4] += lst[i]
    return lst[end]


start = time.time()
print(cnt(2, 70) - cnt(2, 35) * cnt(35, 70), end=" ")
end = time.time()
print(end - start)

# I think it`s slowly
start = time.time()
lst = [0] * 71 * 4
lst[2] = 1
for i in range(2, 71):
    if i + 1 != 35:
        lst[i + 1] += lst[i]
    if i * 3 != 35:
        lst[i * 3] += lst[i]
    if i * 4 != 35:
        lst[i * 4] += lst[i]
end = time.time()
print(lst[70], end - start)
