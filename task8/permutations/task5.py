from itertools import permutations

lst = list(set(map("".join, permutations("АВРОРА", r=6))))
cnt = 0
for i in lst:
    for j in set("АВРОРА"):
        if j * 2 in i:
            break
    else:
        cnt += 1
print(cnt)
