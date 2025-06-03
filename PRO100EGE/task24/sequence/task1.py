with open("../data/j6.txt") as f:
    line = f.readline()
    cnt = 1
    mx = 0
    for i in range(1, len(line)):
        if int(line[i - 1]) < int(line[i]):
            cnt += 1
        else:
            if cnt == 5:
                mx += 1
            cnt = 1
    if cnt == 5:
        mx += 1
    print(mx)
