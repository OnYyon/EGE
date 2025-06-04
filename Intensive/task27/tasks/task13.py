clA = [[] for i in range(3)]

for s in open('data/27A_19747.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x>5 and y>5: clA[0].append([x,y])
    elif x>5: clA[1].append([x,y])
    else: clA[2].append([x,y])
print([len(cl) for cl in clA])

clB = [[] for i in range(5)]

for s in open('data/27B_19747.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x>10 and y<10: clB[0].append([x,y])
    elif y>10 and y<x: clB[1].append([x,y])
    elif y>x and x>10: clB[2].append([x,y])
    elif y>x: clB[3].append([x,y])
    else: clB[4].append([x,y])
print([len(cl) for cl in clB])

from math import dist

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

cenA = [centr(cl) for cl in clA]
px = sum(x for x,y in cenA)/len(cenA)
py = sum(y for x,y in cenA)/len(cenA)
print(int(abs(px*100_000)//1), int(abs(py*100_000)//1))

cenB = [centr(cl) for cl in clB]
px = sum(x for x,y in cenB)/len(cenB)
py = sum(y for x,y in cenB)/len(cenB)
print(int(abs(px*100_000)//1), int(abs(py*100_000)//1))
