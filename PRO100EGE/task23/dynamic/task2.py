lst = [1] + [0] * 15
for i in range(1, 16):
    if (i + 1) % 2 == 0:
        lst[i] += lst[i // 2]
    if i - 3 >= 0:
        lst[i] += lst[i - 3]

print(lst)
