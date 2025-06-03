with open("../data/24-263.txt") as f:
    line = f.readline().replace("BAD", "t").replace("FAT", "t")
    mn = 1000
    # TODO: добавить 6

    for l in range(len(line)):
        for r in range(l + mn, l, -1):
            pattern = line[l:r + 1]
            if pattern.count("t") <= 3:
                if pattern.count("t") == 3:
                    mn = min(mn, len(pattern) + 6)
            else:
                break
    print(mn)
