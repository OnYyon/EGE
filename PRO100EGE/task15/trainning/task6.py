a = 0
last_x = 20 - 0.25
for x in [i * 0.25 for i in range(80, 321)]:
     p = 20 <= x <= 80
     q = 35 <= x <= 57
     if a and (q <= p) != 0:
         print(x, x - last_x)
     last_x = x
