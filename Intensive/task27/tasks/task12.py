from math import dist

clA = [[], [], []]
clB = [[], [], [], [], [], []]

with open("data/27_A_21599.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if y < -5:
            clA[0].append([x, y])
        elif y > 1.625 * x - 19.625:
            clA[1].append([x, y])
        else:
            clA[2].append([x, y])

with open("data/27_B_21599.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if y < -5:
            clB[0].append([x, y])
        elif y < 0.5*x:
            clB[1].append([x, y])
        elif y < 1.5 * x + 10:
            clB[2].append([x, y])
        elif x > -10:
            clB[3].append([x, y])
        elif y > -2 * x - 25:
            clB[4].append([x, y])
        else:
            clB[5].append([x, y])


def center(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return min(lst)[1]

centerA = [center(cl) for cl in clA]
px = sum(x for x, _ in centerA) / len(clA)
py = sum(y for _, y in centerA) / len(clA)
print(int(abs(px * 10000) // 1), int(abs(py * 10000) // 1))

centerB = [center(cl) for cl in clB]
px = sum(x for x, _ in centerB) / len(clB)
py = sum(y for _, y in centerB) / len(clB)
print(int(abs(px * 10000) // 1), int(abs(py * 10000) // 1))
