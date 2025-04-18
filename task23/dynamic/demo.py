lst = [1] + [0] * 5
for i in range(1, 6):
    if i - 1 >= 0:
        lst[i] += lst[i - 1]
    if i - 3 >= 0:
        lst[i] += lst[i - 3]
print(lst[5])
