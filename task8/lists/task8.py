from itertools import product

lst = list(map("".join, product(sorted("ПРЕСТОЛ"), repeat=5)))
cnt = 0
for i in range(len(lst)):
    for j in "ПРСТЛ":
        lst[i] = lst[i].replace(j, "t")
    if lst[i][-1] in ["Е", "О"] and lst[i].count("t") <= 3 and i % 2 == 0:
        print(lst[i], i)
        cnt += 1
print(cnt)
