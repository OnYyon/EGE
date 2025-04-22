# import re
with open("../data/k7a-6.txt") as f:
    line = f.readline()
    # lst = re.findall(r"B{1,}", line)
    # print(len(max(lst, key=lambda x: len(x))))
    count = 0
    mx = -1
    for s in range(0, len(line)):
        if line[s] == 'B':
            count += 1
        else:
            count = 0
        if count > mx:
            mx = count
    print(mx)
