from itertools import product

lst = list(map(lambda x: "".join(x), product(list("ШКОЛА"), repeat=3)))
lst = list(filter(lambda x: x.count("К") == 1, lst))
print(lst, len(lst), sep="\n")
