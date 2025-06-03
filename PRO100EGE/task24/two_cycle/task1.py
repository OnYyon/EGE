with open("../data/24-295.txt") as f:
    line = f.readline()
    mx = 0

    for l in range(len(line)):
        for r in range(l, len(line)):
            pattern = line[l:r + 1]
            if pattern.count("DE") <= 240:
                mx = max(mx, len(pattern))
            else:
                break
    print(mx)
