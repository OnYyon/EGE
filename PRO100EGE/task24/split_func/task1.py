with open("../data/24-j5.txt", "r") as  f:
    line = f.readline()
    line = line.replace("STOCK", "!")
    line = line.replace("OCK", "L")
    print(line.count("L"))