lst = [0] * 100
lst[1] = 1
lst[2] = 7
lst[3] = 1
for i in range(4, 51):
    if i % 2 == 0:
        lst[i] = 6 + lst[i - 1] + lst[i - 2]
    else:
        lst[i] = lst[i - 1] + lst[i - 2]

print(lst[50])
