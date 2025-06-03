lst = [0] * 100 * 4
lst[2] = 1
for i in range(2, 100):
    lst[44] = 0
    lst[i + 5] += lst[i]
    lst[i * 3] += lst[i]
    lst[i * 4] += lst[i]

print(lst[99])
