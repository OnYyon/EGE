from itertools import permutations

lst = list(set(map("".join, permutations("ГОВОР", r=5))))
cnt = 0
for i in lst:
    if "ОО" not in i:
        cnt += 1
print(cnt)
