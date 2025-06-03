cnt = 0
for p1 in "1234567":
    for p2 in "01234567":
        for p3 in "01234567":
            for p4 in "01234567":
                for p5 in "01234567":
                    number = p1 + p2 + p3 + p4 + p5
                    not_vogel = list("1357")
                    if number[0] not in not_vogel and number[-1] not in ["2", "6"] and number.count("7") <= 2:
                        cnt += 1
print(cnt)
