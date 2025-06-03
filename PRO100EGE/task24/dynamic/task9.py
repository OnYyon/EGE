from itertools import product

with open("../data/24(1).txt") as f:
    line = f.readline().replace('A','*').replace('B','*').replace('C','*')
    # Так как мы можем добавить по одной букве слева и справа
    # print(len(max(line.split("**"), key=len)) + 2)
    patterns = list(map("".join, product("ABC", repeat=2)))
    lst = [0] * (len(line) + 1)
    lst[1] = 1
    for i in range(2, len(line)):
         if line[i - 1:i + 1] not in patterns:
             lst[i] = lst[i - 1] + 1
         else:
             lst[i] = 1
    print(max(lst))
