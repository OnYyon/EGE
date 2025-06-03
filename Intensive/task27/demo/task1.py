from math import dist

clA = [[], []]
clB = [[], [], []]

with open("data/27A_1.txt") as f:
    f.readline()
    for line in f.readlines():
        x, y = map(float, line.split())        
        if y > -2:
            clA[0].append([x, y])
        else:
            clA[1].append([x, y])


