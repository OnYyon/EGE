with open("../data/1.txt") as f:
    line = f.readline()
    mx = 0
    k = 1
    start = 0
    for i in range(1, len(line)):
        if line[i] < line[i - 1]:
            k += 1
        else:
            if mx < k:
                mx = k
                start = i - k + 1
            k = 1
    print(start, mx)
