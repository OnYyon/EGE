cnt = 0
for p1 in "123456789ABCDEF":
    for p2 in "0123456789ABCDEF":
        for p3 in "0123456789ABCDEF":
            for p4 in "0123456789ABCDEF":
                number = p1 + p2 + p3 + p4
                t = number[:]
                for i in "02468ACE":
                    t = t.replace(i, "t")
                for i in "13579BDF":
                    t = t.replace(i, "n")
                if len(set(number)) == 4 and "tt" not in t and "nn" not in t:
                    cnt += 1
                    print(number, t)
print(cnt)
