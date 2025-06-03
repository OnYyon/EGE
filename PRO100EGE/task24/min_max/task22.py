with open("../data/j7.txt") as f:
    line = f.readline().strip()
    cnt = 1
    mx = 0
    for i in range(1, len(line)):
        if int(line[i]) % 2 == int(line[i - 1]) % 2:
            cnt += 1
        else:
            cnt = 1
        if cnt > mx:
            mx = cnt
    print(mx)
