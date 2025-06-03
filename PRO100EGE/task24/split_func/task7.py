f = open('../data/s1.txt')
otv = 0

for s in f:
    count = 0
    for i in range(3, len(s)):
        if s[i - 3] == 'E' and s[i] == 'R':
            count += 1

    if count > 3:
        otv += 1

print(otv)