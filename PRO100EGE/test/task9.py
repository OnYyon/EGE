with open("9_21704.txt") as f:
    cnt = 0
    for line in f.readlines():
        lst = list(map(int, line.strip().split(";")))
        t = sorted(lst)
        if sorted(lst, reverse=True) == lst and (t[0] + t[-1]) / 2 > (t[1] + t[2] + t[3] + t[4] + t[5]) / 5:
            print(sum(lst))
            break
