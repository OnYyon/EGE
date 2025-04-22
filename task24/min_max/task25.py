with open("../data/157.txt") as f:
    line = f.readline().strip()
    cnt = 1
    mx = 0
    for i in range(1, len(line)):
        if line[i] + line[i - 1] not in ["PR", "RP"]:
            cnt += 1
        else:
            cnt = 1
        mx = max(cnt, mx)
    print(mx)
