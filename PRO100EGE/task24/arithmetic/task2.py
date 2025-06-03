with open("../data/In7Bbmjp3.txt") as f:
    line = f.readline().strip().strip("+")
    # line = line.replace("++", " ").replace(" +", " ")
    # print(max(filter(lambda x: "+" in x, line.split()), key=len))
    lst = line.split("+")
    mx = -1
    cnt = []
    for i in range(len(lst)):
        if lst[i]:
            cnt.append(lst[i])
        else:
            if len(cnt) > 1:
                if mx < sum(map(len, cnt)) + len(cnt) - 1:
                    mx = sum(map(len, cnt)) + len(cnt) - 1
            cnt = []
    if mx < sum(map(len, cnt)) + len(cnt) - 1:
        mx = sum(map(len, cnt)) + len(cnt) - 1
    print(mx)

# 34937+7549431185692+56634161885+445893921784+37658262676371+31339528944718+64828528+7937393738842+37886+5329367+2929+73+7577344195+61179687+92878773413+1246599172