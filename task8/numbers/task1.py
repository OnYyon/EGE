count = 0
for p1 in "246":
    for p2 in "01234567":
        for p3 in "01234567":
            for p4 in "567":
                number = p1 + p2 + p3 + p4
                if number.count("6") > 2:
                    count += 1
print(count)
