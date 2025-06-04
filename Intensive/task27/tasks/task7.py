from math import dist


def db_scan(r, path_to_file, min_cluster):
    data = []
    with open(path_to_file) as f:
        f.readline()
        for line in f.readlines():
            x, y = map(float, line.replace(",", ".").split())
            data.append([x, y])

    clusters = []
    while data:
        cl = [data.pop()]
        for p in cl:
            sosedi = [p1 for p1 in data if dist(p, p1) < r]
            for p1 in sosedi:
                cl.append(p1)
                data.remove(p1)
        clusters.append(cl)
    return list(filter(lambda x: len(x) >= min_cluster, clusters))

def center(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return min(lst)[1]


clA = db_scan(1, "data/27A_18056.txt", 30)
clB = db_scan(0.5, "data/27B_18056.txt", 30)

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

centerA = [center(cl) for cl in clA]
px = sum(x for x, _ in centerA) / len(clA)
py = sum(y for _, y in centerA) / len(clA)
print(int(abs(px * 100_000)//1), int(abs(py * 100_000)//1))

centerB = [center(cl) for cl in clB]
px = sum(x for x, _ in centerB) / len(clB)
py = sum(y for _, y in centerB) / len(clB)
print(int(abs(px * 100_000)//1), int(abs(py * 100_000)//1))
