# a -> b == not(a) or b
# a -> b == a <= b
def check(a):
    for x in range(100000):
        f1 = x % a == 0
        f2 = x % 6 == 0
        f3 = x % 4 == 0
        if (not(not(f1)) or (not(f2) or not(f3))) != 1:
            return False
    return True

for i in range(1, 100000):
    if check(i):
        print(i)
