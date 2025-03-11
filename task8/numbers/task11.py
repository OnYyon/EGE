cnt = 0
for p1 in "123456789":
    for p2 in "0123456789":
        for p3 in "0123456789":
            for p4 in "0123456789":
                for p5 in "0123456789":
                    number = p1 + p2 + p3 + p4 + p5
                    t = number[:]
                    for i in "02468ACE":
                        t = t.replace(i, "t")
                    for i in "13579BDF":
                        t = t.replace(i, "n")
                    if len(set(number)) == 5 and "tt" not in t and "nn" not in t and "5" not in number:
                        cnt += 1
print(cnt)
