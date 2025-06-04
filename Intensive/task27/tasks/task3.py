from math import dist

def db_scan(r: float, path_to_file: str, min_cluster: int):
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
    return  clusters


clA = db_scan(1, "data/27_A_21931.txt", 1)
clB = db_scan(1, "data/27_B_21931.txt", 1)

def anticenter(cl):
    lst = []
    for p in cl:
        s = sum(dist(p, p1) for p1 in cl)
        lst.append([s, p])
    return max(lst)[1]

px = anticenter(min(clA, key=len))
py = anticenter(max(clA, key=len))
print(int(px[0]*10000//1), int(py[1]*10000//1))

px = anticenter(min(clB, key=len))[0]
py = anticenter(max(clB, key=len))[1]
print(int(px*10000//1), int(py*10000//1))
