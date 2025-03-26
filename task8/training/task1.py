from itertools import product

lst = list(map("".join, product(sorted("ДЕЖЗИК"), repeat=3)))
cnt = 0
for i in lst:
    if i.count("И") == 1 and i.count("Е") == 0 or i.count("И") == 0 and i.count("Е") == 1:
        cnt += 1
print(cnt)
