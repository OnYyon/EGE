with open("../data/bI4DufyyF(1).txt") as f:
    line = f.readline().strip().strip("*").strip("-").replace("-", "*")
    t = line[0]
    ans = -1
    is_op_in = 0
    for i in range(1, len(line)):
        t += line[i]
        if line[i] in "0789":
            if is_op_in and not any(map(lambda x: x[0] == "0", t.split("*"))):
                ans = max(len(t), ans)
                print(t)
        else:
            is_op_in = 1
            if line[i - 1] == '*':
                t = ''
                is_op_in = 0
    print(ans)
