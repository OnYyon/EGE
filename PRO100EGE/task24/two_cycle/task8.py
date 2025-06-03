from string import ascii_uppercase


def my_replace(string):
    for i in ascii_uppercase:
        string = string.replace(i, "t")
    for i in "0123456789":
        string = string.replace(i, "n")
    return string


with open("../data/24-264.txt") as f:
    line = my_replace(f.readline())
    mx = 0

    for l in range(len(line)):
        for r in range(l + mx, len(line)):
            pattern = line[l:r + 1]
            if "tt" not in pattern and "nn" not in pattern:
                mx = max(len(pattern), mx)
            else:
                break
    print(mx)
