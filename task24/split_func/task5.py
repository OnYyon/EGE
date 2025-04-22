with open("../data/5.txt", "r") as f:
    line = f.readline()
    cnt = 0
    for i in range(len(line)):
        if line[i:i+2] == "()":
            cnt += 1
        if cnt == 10000:
            print(i + 1)
            break
