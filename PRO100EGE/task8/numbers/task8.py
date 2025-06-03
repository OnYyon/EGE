cnt = 0
for p1 in "12345":
    for p2 in "012345":
        for p3 in "012345":
            for p4 in "012345":
                for p5 in "012345":
                    for p6 in "012345":
                        number = p1 + p2 + p3 + p4 + p5 + p6
                        for i in "135":
                            number = number.replace(i, "n")
                        if number.count("2") == 1 and "n2" not in number and "2n" not in number:
                            cnt += 1
print(cnt)
