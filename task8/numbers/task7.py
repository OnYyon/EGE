cnt = 0
for p1 in "12345678":
    for p2 in "012345678":
        for p3 in "012345678":
            for p4 in "012345678":
                for p5 in "012345678":
                    number = p1 + p2 + p3 + p4 + p5
                    for i in "02468":
                        number = number.replace(i, "n")
                    print(number)
                    if number.count("1") == 1:
                        if "n1" not in number and "1n" not in number:
                            cnt += 1
print(cnt)
