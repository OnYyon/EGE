a = 0
cnt = 0
lst1 = list(range(2, 21, 2))
lst2 = list(range(3, 31, 3))
for x in range(1, 100500):
    p = x in lst1
    q = x in lst2
    if ((p <= a) or ((not a) <= (not q))) == 0:
        print(x)
        cnt += 1
print(cnt)
