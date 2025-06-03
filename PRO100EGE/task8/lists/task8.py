from itertools import product

lst = list(map("".join, product(sorted("УЖЕМАЙ"), repeat=5)))
cnt = 0
for i in range(len(lst)):
    if i % 2 == 1:
        flag = True
        for j in "УЖЕМАЙ":
            if j * 2 in lst[i]:
                flag = False
        if flag:
            cnt += 1
print(cnt)
