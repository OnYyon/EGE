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


clA = db_scan(1, "data/27A_20295.txt")
clB = db_scan(0.4, "data/27B_20295.txt")


def metrics(cl):
    lst = []
    for p in cl:
        avg = sum([1 for p1 in cl if dist(p, p1) <= 1])
        lst.append(avg)
    return sum(lst)/len(lst)


avgA = [metrics(cl) for cl in clA]
pmin = min(avgA)
pavg = sum(avgA) / len(avgA)
print(int(pmin * 100_000), int(pavg * 100_000))

avgB = [metrics(cl) for cl in clB]
pmin = min(avgB)
pavg = sum(avgB) / len(avgB)
print(int(pmin * 100_000 // 1), int(pavg * 100_000 // 1))
