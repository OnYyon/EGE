with open("../data/1.txt") as f:
    s = f.readline()
    k = 1
    maxx = 0
    for i in range(1, len(s)):
        if s[i - 1] < s[i]:
            k += 1
            if k > maxx:
                maxx = k
                smax = s[i - k + 1: i + 1]  # Зная позицию последнего символа в подстроке i
                # и его длину k, можно с помощью среза получить саму
                # подстроку. Не забудьте, что в срезе правая граница не
                # включается!
        else:
            k = 1
    print(smax, maxx)
