cnt = 0
for p1 in "1246":
    for p2 in "0123456":
        for p3 in "0123456":
            for p4 in "0123456":
                for p5 in "0123456":
                    for p6 in "0123456":
                        for p7 in "0123456":
                            number = p1 + p2 + p3 + p4 + p5 + p6 + p7
                            if ("22" in number) + ("44" in number) < 2:
                                cnt += 1
print(cnt)
