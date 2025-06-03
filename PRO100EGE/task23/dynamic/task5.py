# First variant(not template)
lst = [0] * 13
lst[3] = 1
for i in range(3, 11):
    lst[i + 2] += lst[i]
    if i * 2 <= 12:
        lst[i * 2] += lst[i]

print(lst)

# Second variant(template)
lst = [0] * 100
lst[3] = 1
for i in range(3, 12):
    lst[i + 2] += lst[i]
    lst[i * 2] += lst[i]

print(lst[12])
