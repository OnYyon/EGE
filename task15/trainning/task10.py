a = 0
prev_x = 4 - 0.25
for x in [i * 0.25 for i in range(16, 81)]:
    p = 4 <= x <= 15
    q = 12 <= x <= 20
    if ((p and q) <= a) != 1:
        print(x, x - prev_x)
    prev_x = x
