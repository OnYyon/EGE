from math import dist

clA = [[], []]
clB = [[], [], []]

with open("data/27_A_21929.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if y < 12:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])

with open("data/27_B_21929.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if y < 12:
            clB[0].append([x, y])
        elif x > 17:
            clB[1].append([x, y])
        else:
            clB[2].append([x, y])

def center(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return min(lst)[1]

cenA = [center(cl) for cl in clA]
px = sum(x for x,y in cenA)/len(cenA)
py = sum(y for x,y in cenA)/len(cenA)
print(int(px*10000//1), int(py*10000//1))

cenB = [center(cl) for cl in clB]
px = sum(x for x,y in cenB)/len(cenB)
py = sum(y for x,y in cenB)/len(cenB)
print(int(px*10000//1), int(py*10000//1))
