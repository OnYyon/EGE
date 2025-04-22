with open("../data/24-j8.txt") as f:
    line = f.readline().strip()
    mx = 0
    k = 1
    for i in range(len(line) - 1):
        if int(line[i]) + int(line[i + 1]) >= 10:
            k += 1
        else:
            if mx < k:
                mx = k
            k = 1
    print(mx)
