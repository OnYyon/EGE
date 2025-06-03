a = 0
p = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
cnt = 0
for x in range(1, 100500):
    fp = x in p
    fq = x in q
    if ((fp <= a) or ((not a) <= (not fq))) != 1:
        print(x)
        cnt += 1
print(cnt)
