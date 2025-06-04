clA = [[], []]
clB = [[], [], []]

with open("data/27A_2_20207.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if x > 4:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])

with open("data/27B_2_20207.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if x > 4:
            clB[0].append([x, y])
        elif y > 6:
            clB[1].append([x, y])
        else:
            clB[2].append([x, y])


def medianaX(cl):
    for p in cl:
        k = len([p1 for p1 in cl if p1[0] > p[0]])
        if k == len(cl)//2:
            return p

def medianaY(cl):
    for p in cl:
        k = len([p1 for p1 in cl if p1[1] > p[1]])
        if k == len(cl)//2:
            return p


medianaAX = [medianaX(cl) for cl in clA]
medianaAY = [medianaY(cl) for cl in clA]
px = sum(x for x, _ in medianaAX) / len(clA)
py = sum(y for _, y in medianaAY) / len(clA)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))

medianaBX = [medianaX(cl) for cl in clB]
medianaBY = [medianaY(cl) for cl in clB]
px = sum(x for x, _ in medianaBX) / len(clB)
py = sum(y for _, y in medianaBY) / len(clB)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))
