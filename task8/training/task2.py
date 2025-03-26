cnt = 0
for p1 in "1234567":
    for p2 in "01234567":
        for p3 in "01234567":
            for p4 in "01234567":
                for p5 in "01234567":
                    for p6 in "01234567":
                        number = p1 + p2 + p3 + p4 + p5 + p6
                        number = number.replace("1", "t").replace("3", "t").replace("5", "t").replace("7", "t")
                        if number.count("6") == 2 and "t6" not in number and "6t" not in number:
                            cnt += 1
print(cnt)
