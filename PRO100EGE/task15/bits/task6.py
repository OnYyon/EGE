a = 0
p = list(range(2, 21, 2))
q = list(range(3, 31, 3))
for x in range(1, 100500):
    fp = x in p
    fq = x in q
    if ((fp <= a) or ((not a) <= (not fq))) != 1:
        print(x)
