f = open('17-354.txt')
a = [int(x) for x in f]
b = [c for c in a if abs(c) % 10 == 1]
b1 = min(b)

max1 = -1e20
k = 0
for i in range(0, len(a) - 1):
    if (abs(a[i]) % 10) == (abs(a[i + 1]) % 10):
        if ((a[i] % 3 == 0) + (a[i + 1] % 3 == 0)) == 1:
            if (a[i]**2 + a[i + 1]**2) <= b1**2:
                k += 1
                max1 = max(max1, a[i] + a[i + 1])
print(k, max1)