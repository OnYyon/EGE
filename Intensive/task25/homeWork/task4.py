from itertools import product, repeat

sm = 0
cnt = 0
for star_length in range(7):
    for a in range(10):
        for star in product("0123456789", repeat=star_length):
            x = int(f"1{"".join(star)}28{a}{64}")
            if x % 596 == 0:
                cnt += 1
                sm += x

print(cnt, sm / cnt)
