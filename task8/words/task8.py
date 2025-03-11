from itertools import product

lst = list(map("".join, product("ПАУК", repeat=5)))
cnt = 0
for i in lst:
    is_vowel = set(i) & {"А", "У"}
    if len(is_vowel) == 1 and i.count(list(is_vowel)[0]) == 1:
        cnt += 1
        print(i, is_vowel)
print(cnt)
