alphabet = "0123456789ABCDEF"
cnt = 0
for p1 in "23456789ABCDEF":
    for p2 in "0123456789ABCDEF":
        for p3 in "0123456789ABCDEF":
            for p4 in "0123456789ABCDEF":
                for p5 in "A":
                    for p6 in "B":
                        cnt += 1
print(cnt)
