# P = [15, 30] и Q = [5, 60]
# (¬(x ∈ Q) ∨ (x ∈ P)) ∧ (x ∈ A)
a = 1
last_x = 0
for x in [i * 0.25 for i in range(60 * 4 + 1)]:
    p = 15 <= x <= 30
    q = 5 <= x <= 60
    f = ((not q) or p) and a
    if f == 0:
        print(x - last_x, x)
        last_x = x

# f - 30.25
# 1 - 30.25 - 5.25
# 2 - 60 - 30.35