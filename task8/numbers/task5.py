cnt = 0
for p1 in "124568":
    for p2 in "012345678":
        for p3 in "012345678":
            for p4 in "012345678":
                for p5 in "012345678":
                    for p6 in "012345678":
                        for p7 in "012345678":
                            number = p1 + p2 + p3 + p4 + p5 + p6 + p7
                            if ("00" in number) + ("11" in number) + ("22" in number) + ("33" in number) + \
                                ("44" in number) + ("55" in number) + ("66" in number) + ("77" in number) + \
                                ("88" in number) == 0:
                                cnt += 1
print(cnt)
