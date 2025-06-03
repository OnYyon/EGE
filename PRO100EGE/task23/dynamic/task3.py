lst = [0]* 152
lst[3] = 1
for i in range(4, 152):
    lst[i] += lst[i - 4]
    if i % 5 == 0:
        lst[i] += lst[i // 5]

print(lst[-1])
