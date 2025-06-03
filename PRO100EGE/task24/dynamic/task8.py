with open("../data/24-180.txt") as f:
    line = f.readline()
    lst = [0] * (len(line) + 1)
    for i in range(4, len(line)):
        if 0 <= int(line[i - 3:i - 1]) <= 23 and 0 <= int(line[i-1:i+1]) <= 59:
            lst[i] = lst[i - 4] + 1
    print(max(lst))
