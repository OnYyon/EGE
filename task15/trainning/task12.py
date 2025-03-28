a = 0
prev_x = 6 - 0.25
for x in [i * 0.25 for i in range(24, 209)]:
    p = 6 <= x <= 45
    q = 18 <= x <= 52
    if ((q == p) or ((p and (not q)) <= a)) != 1:
        print(x, x - prev_x)
        prev_x = x
