with open("../data/24-280.txt") as f:
    line = f.readline()
    mx = 0
    for l in range(len(line)):
        for r in  range(l + mx, len(line)):
            pattern = line[l:r + 1]
            flag = all(map(lambda x: x <= 10, {i: pattern.count(i) for i in set(pattern)}.values()))
            if flag:
                mx = max(len(pattern), mx)
            else:
                break
    print(mx)
