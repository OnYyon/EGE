with open("../data/24-153.txt") as f:
    line = filter(lambda x: x, f.readline().split("D"))
    print(len(max(line, key=lambda x: len(x))) + 2)
