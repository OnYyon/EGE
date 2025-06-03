a = 0
last_x = 36.75
for x in [i * 0.25 for i in range(148, 308)]:
    p = 37 <= x <= 60
    q = 40 <= x <= 77
    if (p <= ((q and (not a)) <= (not p))) != 1:
        print(x, x - last_x)
    last_x = x
