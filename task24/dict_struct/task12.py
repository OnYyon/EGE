import re
with open("../data/s2.txt") as f:
    line = f.readline()
    lst = map(lambda x: x[1], re.findall(r"X.Y", line))
    d = dict()
    for s in lst:
        if not d.get(s):
            d[s] = 1
        else:
            d[s] += 1
    print(*max(d.items(), key=lambda x: (x[1], x[0])), sep="")
