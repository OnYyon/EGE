# TODO: нужная подстрока находиться в большой подстроке
with open("../data/IGVcRTjyP.txt") as f:
    line = f.readline().strip()
    t = line[0]
    ans = -1
    is_op_in = 0
    for i in range(1, len(line)):
        t += line[i]
        if line[i] in "0123456789":
            if is_op_in and eval(t) == 0:
                ans = max(len(t), ans)
        else:
            is_op_in = 1
            if line[i - 1] in ["*", "+"]:
                is_op_in = 0
                t = ""
                continue
    print(ans, t)

# 0+0+0+41694*0*14755+0+0+0*0*30608*0+0*0+0*0+0*0+0*0*22180*0*0*0+0*0*0*0*0*0+95070*0*0+0+0*0*0*0+0+0+0*58769*0*0*0+0+0+0+0*0*0*0+0+7800*0*0+0+0