a = 1
prev_x = 0.75
for x in [i * 0.25 for i in range(4, 233)]:
    p = 1 <= x <= 39
    q = 23 <= x <= 58
    if ((p <= (not q)) <= (not a)) == 1:
        print(x, x - prev_x)
    prev_x = x