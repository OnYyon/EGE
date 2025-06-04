from itertools import product

lst =  list(map("".join, product(sorted("ГАФНИЙ"), repeat=4)))
cnt =  0
for i in lst:
    if i[0] != "Й" and ("А" in i or "И" in i):
        cnt += 1
        print(i)
print(cnt)
