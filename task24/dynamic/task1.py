with open("../data/24-213.txt") as f:
    line = "*" + f.readline()
    cnt = 0
    mx = 0
    lst = [0] * len(line)
    for i in range(3, len(line)):
        if line[i - 3:i] in ["NPO", "PNO"]:
            lst[i] = lst[i - 3] + 1
    print(max(lst))
