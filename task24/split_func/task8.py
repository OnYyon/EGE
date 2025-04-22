with open("../data/s2.txt", "r") as f:
    d = {}
    data = f.read()
    for i in range(len(data) - 1):
        if  data[i] == "Q":
            d[data[i + 1]] = 1
            d[data[i + 1]] += 1
    d = sorted(d.items(), key=lambda x: (x[1], ord(x[0])))
    print(d)
