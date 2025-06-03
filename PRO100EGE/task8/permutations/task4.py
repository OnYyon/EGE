from itertools import permutations

lst = list(map("".join, permutations("ЗАПИСЬ", r=6)))
cnt = 0
for i in lst:
    t = i.replace("А", "n").replace("И", "n")
    if i[0] != "Ь" and "nЬ" not in t:
        cnt += 1
print(cnt)
