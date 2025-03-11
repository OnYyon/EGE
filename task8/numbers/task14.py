cnt = 0
for p1 in "124567":
    for p2 in "0124567":
        for p3 in "0124567":
            for p4 in "0124567":
                for p5 in "0124567":
                    for p6 in "0124567":
                        number = p1 + p2 + p3 + p4 + p5 + p6
                        t = number[:]
                        for i in "0246":
                            t = t.replace(i, "t")
                        if len(set(number)) == 6 and "tt" in t:
                            cnt += 1
print(cnt)
