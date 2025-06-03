cnt = 0
for p1 in "123456789AB":
    for p2 in "0123456789AB":
        for p3 in "0123456789AB":
            for p4 in "0123456789AB":
                for p5 in "0123456789AB":
                    number = p1 + p2 + p3 + p4 + p5
                    cnts = [number.count(i) for i in "9AB"]
                    if sum(cnts) <=3 and number.count("7") == 1:
                        cnt += 1
print(cnt)
