def convert(s):
    while "42" in s or "8222" in s or "2222" in s:
        if "42" in s:
            s = s.replace("42", "2", 1)
        if "8222" in s:
            s = s.replace("8222", "24", 1)
        if "2222" in s:
            s = s.replace("2222", "8", 1)
    return s



for n in range(4, 10_000):
    s = convert("4" + n * "2")
    if sum(map(int, list(s))) == 110:
        print(n)
        break
