from math import dist


def db_scan(r, path_to_file):
    data = []
    with open(path_to_file) as f:
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

    print([len(cl) for cl in clusters])
    return  list(filter(lambda x: len(x) >= 30, clusters))


clA = db_scan(1, "data/27A_1_20132.txt")
clB = db_scan(1, "data/27B_1_20132.txt")

def metrics(clusters):
    lst = []
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            s = min([[dist(p, p1), p, p1] for p in clusters[i] for p1 in clusters[j]], key=lambda x: x[0])
            lst.append(s[1:])
    return lst


metricsA = metrics(clA)
metricsA = [j for i in metricsA for j in i]
print(metricsA)
px = sum(x for x, _ in metricsA) / len(metricsA)
py = sum(y for _, y in metricsA) / len(metricsA)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))

metricsB = metrics(clB)
metricsB = [j for i in metricsB for j in i]
print(metricsB)
px = sum(x for x, _ in metricsB) / len(metricsB)
py = sum(y for _, y in metricsB) / len(metricsB)
print(int(px * 10_000 // 1), int(py * 10_000 // 1))
