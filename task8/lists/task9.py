from itertools import product

lst = list(map("".join, product(sorted("АПРЕЛЬ", reverse=True), repeat=5)))[:388]
cnt = 0
for i in lst:
    if i[-1] == "Ь":
        cnt += 1
print(cnt)
