with open("../data/s2.txt", "r") as f:
    line = f.readline()
    d = dict()
    for s in line:
        if not d.get(s):
            d[s] = 1
        else:
            d[s] += 1
    print(min(d.items(), key=lambda x: x[1]))
