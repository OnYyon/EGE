def check(a):
    for x in range(1, 100500):
        f1 = x % 12 == 0
        f2 = 70 <= x <= 80
        f3 = x % a == 0
        if (f1 and (f2 and (not f3))) == 1:
            return False
    return True


lst = []
for i in range(1, 100500):
    if check(i):
        lst.append(i)
print(len(lst), lst)
