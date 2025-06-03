lst = [0] * 52
lst[1] = 1
for i in range(5, 52):
    lst[i] += lst[i - 4]
    if i % 5 == 0:
        lst[i] += lst[i // 5]

print(lst)
