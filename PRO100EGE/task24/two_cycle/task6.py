with open("../data/24-280.txt") as f:
    line = f.readline()
    mx = 0

    alphabet = "A, E, I, O, U, Y".split(", ")
    for l in range(len(line)):
        for r in range(l + mx, len(line)):
            pattern = line[l:r + 1]
            flag = all(map(lambda x: x <= 8, [pattern.count(i) for i in alphabet]))
            if flag:
                if all(map(lambda x: x == 8, [pattern.count(i) for i in alphabet])):
                    mx = max(len(pattern), mx)
            else:
                break
    print(mx)
