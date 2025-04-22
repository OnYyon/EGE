with open("../data/j5.txt", "r") as f:
    line = f.readline()
    line = line.replace("KCCTT", "!")
    print(line.count("KCC"))
