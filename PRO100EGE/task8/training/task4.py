from itertools import product

lst = list(map("".join, product(sorted("МАНГУСТ"), repeat=6)))
cnt = 0
for i in range(len(lst) - 1, -1, -1):
    t = lst[i]
    if "У" != t[0] and t.count("М") == 2 and t.count("Г") <= 1:
        print(t, i)
        break
print(cnt)
