cnt = 0
for i in range(237567892, 1134567005):
    n = ((1 + i) * i) // 2
    sm = sum(map(int, list(str(n))))
    print(sm)
