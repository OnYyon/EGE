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

def krai(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return max(lst)[1]


clA = db_scan(0.4, "data/27.19.A_20497.txt")
clB = db_scan(1.6, "data/27.19.B_20497.txt")

kraiA = [krai(cl) for cl in clA]
kraiB = [krai(cl) for cl in clB]

tx = sum(x for x, _ in kraiA) / len(clA)
ty = sum(y for _, y in kraiA) / len(clA)
print(int(abs(tx * 10_000) // 1), int(abs(ty *10_000) // 1))

tx = sum(x for x, _ in kraiB) / len(clB)
ty = sum(y for _, y in kraiB) / len(clB)
print(int(abs(tx * 10_000) // 1), int(abs(ty *10_000) // 1))
