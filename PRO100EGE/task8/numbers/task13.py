cnt = 0
for p1 in "123456789":
    for p2 in "0123456789":
        for p3 in "0123456789":
            for p4 in "0123456789":
                for p5 in "0123456789":
                    for p6 in "05": # Optimize
                        number = p1 + p2 + p3 + p4 + p5 + p6
                        t = number[:]
                        for i in "02468ACE":
                            t = t.replace(i, "t")
                        for i in "13579BDF":
                            t = t.replace(i, "n")
                        if len(set(number)) == 6 and "tt" not in t and "nn" not in t:
                            cnt += 1
print(cnt)
