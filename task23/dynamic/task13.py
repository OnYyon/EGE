lst = [0] * 26 * 2
lst[1] = 1
for i in range(1, 26):
    lst[21] = 0
    lst[i + 1] += lst[i]
    lst[2 * i + 1] += lst[i]

print(lst[25])
