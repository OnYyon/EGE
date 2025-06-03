# ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
a = 1
cnt = 0
set1 = range(2, 21, 2)
set2 = range(5, 51, 5)
for x in range(1, 100500):
    p = x in set1
    q = x in set2
    f = (a <= p) and (q <= (not a))
    if f == 1:
        cnt += 1
        print(x)
print(cnt)
