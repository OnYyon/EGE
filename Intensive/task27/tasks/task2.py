from math import dist

clA = [[], []]
clB = [[], [], []]

with open("data/27_A_21928.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.split())
        if x > 1:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])

with open("data/27_B_21928.txt") as f:
    for line in f.readlines():
        x, y = map(float, line.split())
        if x > 5:
            clB[0].append([x, y])
        elif y > 6:
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
#         goto(x *20, y * 20)
#         dot(3, color)
# done()

def center(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return max(lst)[1]

centerA = [center(cl) for cl in clA]
px = sum(x for x, _ in centerA) / len(clA)
py = sum(y for _, y in centerA) / len(clA)
print(int(px * 10000 // 1), int(py * 10_000 // 1))

centerB = [center(cl) for cl in clB]
px = sum(x for x, _ in centerB) / len(centerB)
py = sum(y for _, y in centerB) / len(centerB)
print(int(px * 10000 // 1), int(py * 10000 // 1))
