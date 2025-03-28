from itertools import permutations

lst = list(map("".join, permutations("КАПКАН", r=6)))
t = []
for i in lst:
    flag = True
    for j in set("КАПКАН"):
        print(j)
        if j * 2 in i:
            flag = False
            break
    if flag:
        t.append(i)
print(len(set(t)))
