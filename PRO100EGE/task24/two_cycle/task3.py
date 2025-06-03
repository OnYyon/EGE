with open("../data/24-280.txt") as f:
    line = f.readline()
    mx = 0

    for l in range(len(line)):
        for r in range(l + mx, len(line)):
            pattern = line[l:r + 1]
            print(pattern)
            if "A" not in pattern and pattern.count("Y") <= 1 and pattern.count("X") <= 1:
                if pattern and pattern.count("Y") == 1 and pattern.count("X") == 1:
                    mx = max(mx, len(pattern))
            else:
                break
    print(mx)
