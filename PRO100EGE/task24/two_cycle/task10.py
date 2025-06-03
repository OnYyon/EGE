with open("../data/24-296.txt") as f:
    line = f.readline()
    mn = 10000

    for l in range(len(line)):
        for r in range(l + mn, l, -1):
            pattern = line[l:r + 1]
            if pattern.count("AF") > 200:
                mn = min(mn, len(pattern))
            else:
                break
    print(mn)
