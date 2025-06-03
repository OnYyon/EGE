a = 0
lst = []
set2 = set(range(2, 21, 2))
set3 = set(range(3, 31, 3))
for x in range(1, 100):
    p = x in set2
    q = x in set3
    f = (p <= a) or ((not a) <= (not q))
    if f != 1:
        print(x)
        lst.append(x)
print(len(lst))
