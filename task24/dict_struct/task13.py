with open("../data/24-157.txt") as f:
    line = f.readline()
    d = dict()
    for i in range(1, len(line) - 1):
        if line[i - 1] == line[i]:
            if not d.get(line[i + 1]):
                d[line[i + 1]] = 1
            else:
                d[line[i + 1]] += 1
    print(*max(d.items(), key=lambda x: (x[1], x[0])), sep="")
