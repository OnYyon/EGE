with open("../data/k7a-3.txt") as f:
    line = f.readline().replace("D", "C").split("C")
    print(len(max(line, key=lambda x: len(x))))
