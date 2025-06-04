from itertools import product

lst = list(map("".join, product(sorted("ШКОЛА"), repeat=3)))

cnt = 0
for i in lst:
    if i.count("К") == 1:
        cnt += 1
print(cnt)
