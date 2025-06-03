with open("../data/24-212.txt") as f:
    line = f.readline()
    for i in "BCD":
        line = line.replace("A"+i, "t")
        line = line.replace("O"+i, "t")
    mx = 0

    for l in range(len(line)):
        for r in range(l + mx, len(line)):
            pattern = line[l:r + 1]
            if set(pattern) == set("t"):
                mx = max(len(pattern), mx)
            else:
                break
    print(mx)
