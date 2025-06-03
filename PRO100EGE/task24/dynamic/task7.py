with open("../data/24-173.txt") as f:
    line = f.readline()
    lst = [0] * len(line)
    lst[4] = 5
    for i in range(5, len(line)):
        if line[i-2:i+1] != line[i-5:i-2]:
            lst[i] = lst[i - 1] + 1
        else:
            lst[i] = 5
    print(max(lst))
