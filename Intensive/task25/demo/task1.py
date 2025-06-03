from fnmatch import *

for x in range(0, 10**9, 13):
    s = str(x)
    if fnmatch(s, "24*68?35") and s[-3] in "39" and \
            set(s[2:-5]) <= set("02468"): # Тут с помощью среза выделяеться вся звездочка
        print(x, x // 13)
