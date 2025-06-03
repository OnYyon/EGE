with open("../data/k7a-1.txt") as f:
    line = f.readline()
    cnt = 0
    mx = 0
    for s in line:
        if s in ["A", "B", "C"]:
            cnt += 1
        else:
            cnt = 0
        if cnt > mx:
            mx = cnt
    print(mx)
