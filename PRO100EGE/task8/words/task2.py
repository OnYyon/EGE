from itertools import product

lst = list(map(lambda x: "".join(x), product(list("ВИШНЯ"), repeat=5)))
lst = list(filter(lambda x: x.count("В") == 2, lst))
print(lst, len(lst), sep="\n")
