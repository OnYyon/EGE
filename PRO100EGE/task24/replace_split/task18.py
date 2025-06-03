with open("../data/k7.txt", "r") as f:
    line = f.readline().replace("B", "A").split("A")
    print(len(max(line, key=lambda x: len(x))))
