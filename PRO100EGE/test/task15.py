a = 1
for x in [i * 0.25 for i in range(-10000, 10000)]:
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    if ((not a) <= (b == c)) != 1:
        print(x)
