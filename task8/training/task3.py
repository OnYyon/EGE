cnt = 0
for p1 in "123456789ABCDEF":
    for p2 in "0123456789ABCDEF":
        for p3 in "0123456789ABCDEF":
            number = p1 + p2 + p3
            if len(set(number)) == 3:
                for i in "02468ACE":
                    number = number.replace(i, "t")
                for i in "13579BDF":
                    number = number.replace(i, "n")
                if "tt" not in number and "nn" not in number:
                    cnt += 1
print(cnt)
