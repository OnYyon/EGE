with open("../data/24-296.txt") as f:
    line = f.readline()
    mx = 0

    for l in range(len(line)):
        for r in range(l + mx, len(line)):
            pattern = line[l:r + 1]
            if pattern.count("CD") == 160:
                mx = max(mx, len(pattern))
            elif pattern.count("CD") < 160:
                continue
            else:
                break
    print(mx)
