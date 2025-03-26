from sympy import false

for p1 in "12345678ABC":
    for p2 in "0123456789ABC":
        for p3 in "0123456789ABC":
            for p4 in "0123456789ABC":
                for p5 in "0123456789ABC":
                    number = p1 + p2 + p3 + p4 + p5
                    d = sorted({i: number.count(i) for i in "0123456789ABC"}.items())
                    flag = True
                    for i in d[7:]:
                        if i[1]

