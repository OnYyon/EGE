cnt = 0
for p1 in "1234567":
    for p2 in "01234567":
        for p3 in "01234567":
            for p4 in "01234567":
                for p5 in "01234567":
                    for p6 in "01234567":
                        for p7 in "01234567":
                            for p8 in "01234567":
                                number = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
                                t = number[:]
                                for i in "02468ACE":
                                    t = t.replace(i, "t")
                                for i in "13579BDF":
                                    t = t.replace(i, "n")
                                if len(set(number)) == 8 and "tt" not in t and "nn" not in t:
                                    cnt += 1
print(cnt)
