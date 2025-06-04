clA = [[], []]
clB = [[], [], []]

with open("data/27A_18054.txt") as f:
    f.readline()
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if x > 3:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])

with open("data/27B_18054.txt") as f:
    f.readline()
    for line in f.readlines():
        x, y = map(float, line.replace(",", ".").split())
        if x > 3:
            clB[0].append([x, y])
        elif y > -2.5:
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
#         goto(x * 20, y * 20)
#         dot(5, color)
# done()


def dist(p, p1):
    return max(abs(p1[0] - p[0]), abs(p1[1] - p[1]))

def center(cl) -> list:
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return min(lst)[1]

cenA = [center(cl) for cl in clA]
px = sum(x for x,y in cenA)/len(cenA)
py = sum(y for x,y in cenA)/len(cenA)
print(int(abs(px*10000)//1), int(abs(py*10000)//1))

cenB = [center(cl) for cl in clB]
px = sum(x for x,y in cenB)/len(cenB)
py = sum(y for x,y in cenB)/len(cenB)
print(int(abs(px*10000)//1), int(abs(py*10000)//1))
