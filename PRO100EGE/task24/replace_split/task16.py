with open("../data/k7a-1.txt") as f:
    line = f.readline().replace("E", "D").split("D")
    print(len(max(line, key=lambda x: len(x))))
