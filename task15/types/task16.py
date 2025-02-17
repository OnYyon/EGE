# Full automatic solution, but so difficult for use

import math
# P = [9, 19] и Q = [24, 54]
# (x ∈ A) → ((x ∈ P) ∨ (x ∈ Q))
a = 1
last_x = 0
for x in [i * 0.25 for i in range(1, 54 * 4 + 1)]:
    p = 9 <= x <= 19
    q = 24 <= x <= 54
    f = a <= (p or q)
    # print(x, last_x)
    if f == 1:
        print(x - last_x)
        last_x = x
