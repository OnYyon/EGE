with open("../data/1.txt") as f:
    line = f.readline()
    start = 0
    mx = 0
    k = 1
    for i in range(1, len(line)):
        if line[i] > line[i - 1]:
            k += 1
        else:
            if mx < k:
                start = i - k + 1
                mx = k
            k = 1
    print(start)
