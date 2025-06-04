clA = [[], []]
clB = [[], [], []]

with open("data/27_A_18314.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if y > 1:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])

with open("data/27_B_18314.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if x > 15:
            clB[0].append([x, y])
        elif y < -5:
            clB[1].append([x, y])
        else:
            clB[2].append([x, y])

# from turtle import *
# from random import random
#
# tracer(0)
# up()
# for cl in clB:
#     color = random(), random(), random()
#     for x, y in cl:
#         goto(x * 10, y * 10)
#         dot(5, color)
# done()

def dist(p, p1):
    return abs(p1[0] - p[0]) + abs(p1[1] - p[1])

def center(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return min(lst)[1]

centerA = [center(cl) for cl in clA]
px = sum(x for x, _ in centerA) / len(clA)
py = sum(y for _, y in centerA) / len(clA)
print(int(abs(px * 1000) // 1), int(abs(py * 1000) // 1))

centerB = [center(cl) for cl in clB]
px = sum(x for x, _ in centerB) / len(clB)
py = sum(y for _, y in centerB) / len(clB)
print(int(abs(px * 1000) // 1), int(abs(py * 1000) // 1))
