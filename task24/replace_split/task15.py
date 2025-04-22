with open("../data/k7a-4.txt") as f:
    line = f.readline().split("A")
    print(len(max(line, key=lambda x: len(x))))
