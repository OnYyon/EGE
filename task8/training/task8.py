# Алфавит: 0, 1, 2, 3
cnt = 0
for p1 in "123":
    for p2 in "0123":
        for p3 in "0123":
            for p4 in "0123":
                for p5 in "0123":
                    number = p1 + p2 + p3 + p4 + p5
                    if number != number[::-1]:
                        cnt += 1
print(cnt)
