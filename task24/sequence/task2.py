with open("../data/j6.txt") as f:
    line = f.readline()
    cnt = 0
    k = 1
    for i in range(1, len(line)):
        if int(line[i]) < int(line[i - 1]):
            k += 1
        else:
            if k == 7:
                cnt += 1
            k = 1
    if k == 7:
        cnt += 1
    print(cnt)
