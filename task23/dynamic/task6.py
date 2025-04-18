lst = [0] * 56 * 4
lst[1] = 1
for i in range(1, 56):
    lst[i + 1] += lst[i]
    lst[i * 4] += lst[i]
print(lst[55])
