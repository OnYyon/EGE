with open("17-410.txt", "r") as f:
    lst = list(map(int, f.readlines()))
    mn = min(lst)
    otvet = []
    for i in range(len(lst) - 1):
        print(lst[i], lst[i + 1])
        if lst[i] % 16 == mn or lst[i + 1] % 16 == mn:
            otvet.append(lst[i] + lst[i + 1])
    print(len(otvet), max(otvet))