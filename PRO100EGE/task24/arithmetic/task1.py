# Первый вариант
from string import ascii_uppercase

with open("../data/o7GIvUMYm(1).txt") as f:
    line = f.readline()
    for i in ascii_uppercase[6:]:
        line = line.replace(i, "*")
    lst = line.split("*")
    print(len(max(lst, key=len)))


# Второй вариант(динамика)
with open("../data/o7GIvUMYm(1).txt" ) as f:
    line = f.readline()
    lst = [0] * (len(line) + 1)
    alphabet = list(map(str, range(10))) + list(ascii_uppercase[:6])
    for i in range(1, len(line)):
        if line[i] in alphabet:
            lst[i] = lst[i - 1] + 1
    print(max(lst))
