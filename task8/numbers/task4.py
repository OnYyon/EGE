cnt = 0
for p1 in "124":
    for p2 in "0123456":
        for p3 in "0123456":
            for p4 in "0123456":
                for p5 in "0123456":
                    for p6 in "0123456":
                        for p7 in "0123456":
                            number = p1 + p2 + p3 + p4 + p5 + p6 + p7
                            if ("12" in number) + ("35" in number) < 2:
                                cnt += 1
print(cnt)
