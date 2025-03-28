from itertools import permutations

lst = list(set(map("".join, permutations("ВОРОТА", r=6))))
cnt = 0
for s in lst:
    if ('ОО' not in s) and ('ОА' not in s) and ('АО' not in s):
        cnt += 1
print(cnt)
