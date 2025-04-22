with open("../data/k7a-6.txt") as f:
    line = f.readline().strip()
    cnt = 0
    mx = 0
    for i in range(len(line)):
        if line[i] in  "BCDF":
            cnt += 1
        else:
            cnt = 0
        mx = max(cnt, mx)
    print(mx)
