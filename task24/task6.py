with open("s1.txt", "r") as f:
    lst = f.readlines()
    print(len(list(filter(lambda x: x.count("O") > x.count("C"), lst))))