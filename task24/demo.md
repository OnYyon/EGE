# 24 таск
## Навигация
- [Полезные приемы и функции](#полезные-приемы-и-функции)

## Полезные приемы и функции
1. **replace + split**
    ```python
    "".replace("???", "???").split("???")
    ```
2. **словари**
    ```python
    with open("../data/s2.txt", "r") as f:
    line = f.readline()
    d = dict()
    for s in line:
        if not d.get(s):
            d[s] = 1
        else:
            d[s] += 1
    print(min(d.items(), key=lambda x: x[1]))
    ```
3. > Определите сколько в файле восходящих последовательностей длиной 5, не входящих в восходящие последовательности большей длины.
    ```python
   with open("../data/j6.txt") as f:
    line = f.readline()
    cnt = 1
    mx = 0
    for i in range(1, len(line)):
        if int(line[i - 1]) < int(line[i]):
            cnt += 1
        else:
            if cnt == 5:
                mx += 1
            cnt = 1
    if cnt == 5:
        mx += 1
    print(mx)
    ```
