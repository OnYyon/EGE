with open("../data/24-249.txt") as f:
    alphabet = "0123456789ABCDEF"
    line = f.readline()
    mn = 1000

    for l in range(len(line)):
        for r in range(l + mn, l, -1):
            pattern = line[l:r + 1]
            if all([i in pattern for i in alphabet]):
                mn = min(len(pattern), mn)
            else:
                break
    print(mn)
