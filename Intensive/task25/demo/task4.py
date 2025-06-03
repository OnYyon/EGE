from fnmatch import fnmatch

for x in range(0, 10 ** 10, 2025):
    if fnmatch(str(x), "33?2*42?") and fnmatch(str(x), "*32??2?"):
        print(x, x // 2025)

# regular exp
# r"24(?:[02468])*68[39]35
