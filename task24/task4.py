with open("j9.txt", "r") as f:
    line = f.readline()
    cnt = 0
    for i in range(len(line) - 8):
        pattern = line[i:i+8]
        if pattern == pattern[::-1]:
            cnt += 1
    print(cnt)