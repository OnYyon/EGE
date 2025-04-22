with open("../data/24-j4.txt", "r") as f:
    line = "!" + f.readline() +  "!"
    cnt = 0
    for i in range(0, len(line) - 5):
        if line[i - 1] != "J" and line[i:i+4] == "BOSS" and line[i + 4] != "J":
           cnt += 1
    print(cnt)
