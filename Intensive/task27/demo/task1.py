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

with open("data/27B_1.txt") as f:
    f.readline()
    for line in f.readlines():
        x, y = map(float, line.split())        
        if y < -5:
            clB[0].append([x, y])
        elif x > -6:
            clB[1].append([x, y])
        else:
            clB[2].append([x, y])

from random import random
# NOTE: for visualize
from turtle import *

tracer(0)
up()
for cl in clB:
    color = random(), random(), random()
    for x, y in cl:
        goto(x * 20, y * 20)
        dot(4, color)
done()
