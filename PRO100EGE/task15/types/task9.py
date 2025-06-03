def check_triangle(a, b, c):
    return a + b > c and a + c > b and c + b > a


def check(a):
    for x in range(1, 10 ** 3):
        f1 = check_triangle(x, 12, 20)
        f2 = max(x, 5) > 28
        f3 = check_triangle(x, a, 3)
        if not((f1 == (not f2)) and f3) == 0:
            return False
    return True


lst = []
for i in range(1, 10 ** 3):
    if check(i):
        lst.append(i)
print(max(lst))
