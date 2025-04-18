lst = [0] * 6801 * 10
lst[68] = 1
for i in range(68, 6801):
    lst[i + 8] += lst[i]
    lst[i * 6] += lst[i]
    lst[i + 6000] += lst[i]
    lst[i * 10] += lst[i]

print(lst[6800])
