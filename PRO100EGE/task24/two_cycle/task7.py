
with open("../data/24-264.txt") as f:
    line = f.readline()
    mx = 0

    for l in range(len(line)):
        for r in  range(l + mx, len(line)):
            pattern = line[l:r + 1]

    print(mx)
