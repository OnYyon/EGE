with open("../data/24-157.txt") as f:
    line = f.readline()
    mx = 0
    k = 1
    for i in range(len(line) - 1):
        if line[i] + line[i + 1] in ["QW", "WQ"]:
            if mx < k:
                mx = k
            k = 1
        else:
            k += 1
    print(mx)
