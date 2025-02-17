a = 0
last_x = 69 - 0.25
for x in [i * 0.25 for i in range(276, 457)]:
    p = 69 <= x <= 91
    q = 77 <= x <= 114
    if (q <= ((p == q) or ((not p) <= a))) != 1:
        print(x, x - last_x)
    last_x = x
